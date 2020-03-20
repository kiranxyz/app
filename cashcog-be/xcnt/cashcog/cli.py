import os
import click
import pytest
from loguru import logger
from dotenv import find_dotenv, load_dotenv


@click.group("cashcog")
def cli():
    pass


@cli.command()
@click.option("--use-dotenv/--skip-dotenv", default=True)
def run_migrations(use_dotenv):
    try:
        from .database import run_migrations as do_run_migrations

        if use_dotenv:
            load_dotenv(find_dotenv())

        do_run_migrations()
    except Exception as e:
        logger.error(e)
        raise


@cli.command()
@click.option("--run-migrations/--no-migrations", default=False)
@click.option("--debug/--no-debug", default=False)
@click.option("--host", type=str, default="0.0.0.0")
@click.option("--port", type=int, default=8080)
@click.option("--use-dotenv/--skip-dotenv", default=True)
def run(run_migrations, debug, host, port, use_dotenv):
    try:
        from .database import run_migrations as do_run_migrations
        from xcnt.cashcog import init_app

        if use_dotenv:
            load_dotenv(find_dotenv())
        if run_migrations:
            do_run_migrations()
        app = init_app()
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        logger.error(e)
        raise


@cli.command()
@click.option("--skip-connection-check/--no-connection-check", default=False)
@click.option("--with-coverage/--no-coverage", default=False)
def run_tests(skip_connection_check, with_coverage):
    import coverage

    cov = None
    if with_coverage:
        cov = coverage.Coverage()
        cov.start()

    from xcnt.cashcog.database import run_connection_check

    if not skip_connection_check:
        run_connection_check()

    test_directory = os.path.join(__file__, "..", "test")
    pytest.main(["--pyargs", test_directory])

    if cov is not None:
        cov.stop()
        cov.save()
