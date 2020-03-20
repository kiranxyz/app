import { CommonModule, DecimalPipe } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FlexLayoutModule } from '@angular/flex-layout';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatButtonModule } from '@angular/material/button'
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule} from '@angular/material/form-field';
import { MatRadioModule} from '@angular/material/radio';
import { MatSelectModule} from '@angular/material/select';
import { MatSlideToggleModule} from '@angular/material/slide-toggle';
import { MatSidenavModule} from '@angular/material/sidenav';
import { MatListModule} from '@angular/material/list';
import { MatCardModule} from '@angular/material/card';
import { MatStepperModule} from '@angular/material/stepper';
import { MatButtonToggleModule} from '@angular/material/button-toggle';
import { MatIconModule} from '@angular/material/icon';
import { MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { MatDialogModule} from '@angular/material/dialog';
import { MatSnackBarModule} from '@angular/material/snack-bar';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table'; 
import { MatCommonModule } from '@angular/material/core';
import { RouterModule } from '@angular/router';

export const CORE_IMPORTS = [
  CommonModule,
  HttpClientModule,
  RouterModule,
];

export const FORMS_IMPORTS = [
  FormsModule,
  ReactiveFormsModule,
];

export const LAYOUT_IMPORTS = [
  FlexLayoutModule,
];

export const MATERIAL_IMPORTS = [
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatCheckboxModule,
  MatCommonModule,
  MatDialogModule,
  MatFormFieldModule,
  MatIconModule,
  MatInputModule,
  MatRadioModule,
  MatSelectModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatStepperModule,
  MatListModule,
  MatSidenavModule,
  MatProgressSpinnerModule,
  MatToolbarModule,
  MatTableModule,
];

export const DEFAULT_IMPORTS = [
  ...CORE_IMPORTS,
  ...FORMS_IMPORTS,
  ...MATERIAL_IMPORTS,
  ...LAYOUT_IMPORTS
];

export const COMPONENTS = [];

export const PROVIDERS = [];

export const DIRECTIVES = [];

export const MODALS = [];

export const PIPES = [];

@NgModule({
  imports: [
    ...DEFAULT_IMPORTS
  ],
  providers: [
    ...PROVIDERS
  ],
  declarations: [
    ...COMPONENTS,
    ...DIRECTIVES,
    ...PIPES,
    ...MODALS
  ],
  entryComponents: [
    ...MODALS
  ],
  exports: [
    ...COMPONENTS,
    ...DIRECTIVES,
    ...PIPES,
    ...DEFAULT_IMPORTS,
    ...MODALS
  ]
})
export class SharedModule { }
