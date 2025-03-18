# ERD (Entity Relationship Diagram)

## ModuleRegistry

- id: PrimaryKey
- name: CharField
- version: CharField
- installed: BooleanField
- enabled: BooleanField
- install_date: DateTimeField
- update_date: DateTimeField
- metadata: JSONField (menyimpan informasi tambahan tentang modul)

## ProductModule (contoh module)

- product_id: PrimaryKey
- name: CharField
- barcode: CharField
- price: DecimalField
- stock: IntegerField
- created_at: DateTimeField
- updated_at: DateTimeField

## Role

- id: PrimaryKey
- name: CharField (manager, user, public)
- permissions: JSONField (menyimpan izin untuk setiap peran)

## UserRole

- id: PrimaryKey
- user_id: ForeignKey (ke User)
- role_id: ForeignKey (ke Role)
