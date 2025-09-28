This is a Django Folder named LibraryProject

# Permissions & Groups Setup

## Custom Permissions
- can_view: User can view books
- can_create: User can add new books
- can_edit: User can edit existing books
- can_delete: User can delete books

## Groups
- Viewers: [can_view]
- Editors: [can_view, can_create, can_edit]
- Admins: [all permissions]

## Usage
Permissions are enforced in views with @permission_required:
- book_list → can_view
- add_book → can_create
- edit_book → can_edit
- delete_book → can_delete

Assign users to groups via Django Admin.