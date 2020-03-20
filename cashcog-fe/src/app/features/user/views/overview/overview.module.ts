import { NgModule } from '@angular/core';

import { SharedModule } from 'shared/shared.module';
import { RouterModule, Routes } from '@angular/router';

import { OverviewComponent } from './overview.component';
import { UserTableComponent } from './components/user-table.component';

const ROUTES: Routes = [
  { path: '', component: OverviewComponent }
];

const COMPONENTS = [
  OverviewComponent,
  UserTableComponent,
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
export class UserOverviewModule { }
