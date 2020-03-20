import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SharedModule } from 'shared/shared.module';

import { NotFoundComponent } from './components/not-found.component';

const COMPONENTS = [
  NotFoundComponent
];


const ROUTES: Routes = [
  {
    path: '', component: NotFoundComponent,
  }
];

@NgModule({
  imports: [
    SharedModule,
    RouterModule.forChild(ROUTES)
  ],
  declarations: [
    ...COMPONENTS
  ]
})
export class NotFoundModule { }
