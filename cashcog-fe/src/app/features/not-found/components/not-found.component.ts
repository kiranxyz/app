import { Component, ChangeDetectionStrategy } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  templateUrl: 'not-found.component.html',
  styleUrls: ['not-found.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class NotFoundComponent {
  constructor(
    private router: Router
  ) { }

  goToHome() {
    this.router.navigate(['/user']);
  }
}
