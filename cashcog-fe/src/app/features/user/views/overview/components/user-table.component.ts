import { Component, Input, Output, ChangeDetectionStrategy, EventEmitter } from '@angular/core';
import { User as IUser } from 'shared/models/user.model';


@Component({
    selector: 'user-table',
    templateUrl: 'user-table.component.html',
    styleUrls: ['user-table.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush
  })
export class UserTableComponent {
    @Input() users: IUser[];
    @Output() onClick = new EventEmitter<IUser>();

    displayedColumns: string[] = [
      'firstName', 'lastName', 'email', 'newsletter', 'createdAt', 'lastModifiedAt', 'delete'
    ];

    shouldShowTable() {
      return this.users.length > 0;
    }

    onDeleteUserClick(user: IUser) {
        this.onClick.emit(user);
    }
}
