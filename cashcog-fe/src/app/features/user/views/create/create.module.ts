import { NgModule } from '@angular/core';

import { SharedModule } from 'shared/shared.module';
import { RouterModule, Routes } from '@angular/router';

import { CreateComponent } from './create.component';
import { FormComponent } from './components/form.component';

const ROUTES: Routes = [
  { path: '', component: CreateComponent }
];

const COMPONENTS = [
  // smart components
  CreateComponent,

  // dumb components
  FormComponent,
];

@NgModule({
  imports: [
    SharedModule,
    RouterModule.forChild(ROUTES),
  ],
  declarations: [
    ...COMPONENTS,
  ],
})
export class UserCreateModule { }
