import { NgModule } from '@angular/core';
import { Routes, RouterModule, PreloadAllModules } from '@angular/router';
import { UserModule } from 'features/user/user.module';
import { NotFoundModule } from 'features/not-found/not-found.module';


const ROUTES: Routes = [
  { path: '', redirectTo: '/user', pathMatch: 'full' },
  { path: 'user', loadChildren: () => UserModule },
  { path: '404', loadChildren: () => NotFoundModule },

  { path: '**', redirectTo: '/404' }
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      ROUTES,
      { preloadingStrategy: PreloadAllModules }
    ),
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
