# PropertyGuard — Project Modify/Delete Update

## Change

Project management now supports authenticated project modification through:

`PATCH /api/v1/projects/{project_id}`

The endpoint updates:

- name
- description
- project_type
- address

Authorization:

- BUILDER: only their own project
- ADMIN: any accessible project
- SUPER_ADMIN: any accessible project
- BUYER: forbidden

Project deletion remains soft deletion through:

`DELETE /api/v1/projects/{project_id}`

Authorization:

- BUILDER: only their own project
- ADMIN: any accessible project
- SUPER_ADMIN: any accessible project
- BUYER: forbidden

No database migration is required for the modify endpoint.
