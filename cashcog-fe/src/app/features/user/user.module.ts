import { NgModule } from '@angular/core';

import { SharedModule } from 'shared/shared.module';
import { RouterModule, Routes } from '@angular/router';
import { UserCreateModule } from './views/create/create.module';
import { UserOverviewModule } from './views/overview/overview.module';

const ROUTES: Routes = [
    { path: '', loadChildren: () => UserOverviewModule },
    { path: 'create', loadChildren: () => UserCreateModule },
];

const COMPONENTS = [];

@NgModule({
  imports: [
    SharedModule,
    RouterModule.forChild(ROUTES),
  ],

  declarations: [
    ...COMPONENTS
  ],

  exports: [
    SharedModule,
    ...COMPONENTS,
  ]
})
export class UserModule { }
