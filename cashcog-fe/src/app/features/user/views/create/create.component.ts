import { Component, ChangeDetectionStrategy } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { MatSnackBar } from "@angular/material/snack-bar";
import { Router } from '@angular/router';

import { Observable } from 'rxjs';
import { FetchResult } from 'apollo-link';

import { UserService } from 'shared/services/user.service';
import { IUserVariables } from 'shared/models/user.model';
import { UserErrors } from 'shared/models/user.model';

@Component({
  templateUrl: 'create.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CreateComponent {
  createUserResult$: Observable<FetchResult>;

  constructor(
    private userService: UserService,
    private router: Router,
    public snackBar: MatSnackBar,
  ) {}

  formSubmit(form: FormGroup) {
    if (form.invalid) { return false; }

    const user: IUserVariables = {
      email: form.get('email')!.value,
      firstName: form.get('firstName')!.value,
      lastName: form.get('lastName')!.value,
      newsletter: !!form.get('newsletter')!.value,
    };

    this.userService.create(user).subscribe((response: any) => {
      if (!response.errors && response.data.createUser.ok) {
        this.router.navigate(['/user']);
      }
      if (response.data.createUser.error || response.errors) {
        const errorMessage = UserErrors[response.data.createUser.error as string].toString();
        this.snackBar.open(errorMessage, "Dismiss", {
          duration: 1500,
        });
      }
    });
  }
}
