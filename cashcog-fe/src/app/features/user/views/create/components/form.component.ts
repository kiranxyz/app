import { Component, OnInit, EventEmitter, Output, ChangeDetectionStrategy } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
    selector: 'user-form',
    templateUrl: 'form.component.html',
    styleUrls: ['form.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush
  })
  export class FormComponent implements OnInit {
    @Output() formSubmit = new EventEmitter<FormGroup>();
    public createUserForm: FormGroup;

    constructor(
      private formBuilder: FormBuilder,
    ) {}

    ngOnInit() {
      this.buildForm();
    }

    onSubmit() {
      if (this.createUserForm.invalid) {
        return false;
      }
      this.formSubmit.emit(this.createUserForm);
    }

    get firstName() { return this.createUserForm.get('firstName')!; }
    get lastName() { return this.createUserForm.get('lastName')!; }
    get email() { return this.createUserForm.get('email')!; }
    get newsletter() { return this.createUserForm.get('newsletter')!; }


    private buildForm() {

      this.createUserForm = this.formBuilder.group({
        firstName: [null, Validators.compose([Validators.required])],
        lastName: [null, Validators.compose([Validators.required])],
        email: [null, Validators.compose([
            Validators.required,
            Validators.pattern(
              "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+[.]+[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
              )
            ])
          ],
        newsletter: [null, null]
      });
    }
  }
