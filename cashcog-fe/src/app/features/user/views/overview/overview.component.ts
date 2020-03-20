import { Component, ChangeDetectionStrategy, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ApolloQueryResult } from 'apollo-client';
import { Observable } from 'rxjs';

import { UserService } from 'shared/services/user.service';
import { User as IUserResponse } from 'shared/models/user.model';

@Component({
  templateUrl: 'overview.component.html',
  styleUrls: ['overview.component.scss'],
})
export class OverviewComponent implements OnInit {
    userResult$: Observable<ApolloQueryResult<IUserResponse>>;

    constructor(
        private userService: UserService,
        private router: Router,
    ) { }

    ngOnInit() {
      this.userResult$ = this.userService.get();
    }

    createUserButtonClick() {
      this.router.navigate(['/user/create']);
    }

    deleteUser(user: IUserResponse) {
      this.userService.delete(user.uuid).subscribe(
        (response: any) => {
          if (!response.errors && response.data.deleteUser.ok) {
            this.userResult$ = this.userService.get();
          }
        }
      );
    }
}
