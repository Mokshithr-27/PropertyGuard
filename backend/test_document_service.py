import uuid

from app.core.database import SessionLocal
from app.models import User, Project, BuilderProfile
from app.services.document_service import create_document


db = SessionLocal()

try:
    # Create a test user
    user = User(
        email=f"document_test_{uuid.uuid4().hex[:8]}@example.com",
        password_hash="test-password-hash",
        full_name="Document Test User",
        is_active=True,
        is_email_verified=True,
    )

    db.add(user)
    db.flush()

    # Create builder profile
    builder = BuilderProfile(
        user_id=user.id,
        company_name="Document Test Builders",
        verification_status="VERIFIED",
    )

    db.add(builder)
    db.flush()

    # Create test project
    project = Project(
        builder_id=builder.id,
        name="Document Test Project",
        description="Test project for PropertyGuard document management.",
        project_type="APARTMENT",
        address="Hyderabad, Telangana",
        status="DRAFT",
    )

    db.add(project)
    db.flush()

    # Test file
    file_data = b"PropertyGuard document upload test successful."

    # Upload document
    document = create_document(
        db=db,
        project_id=project.id,
        uploaded_by=user.id,
        document_type="RERA",
        title="Test RERA Certificate",
        file_name="test_rera.txt",
        mime_type="text/plain",
        data=file_data,
        description="Test document for storage service.",
        visibility="PRIVATE",
    )

    print("Document created successfully!")
    print("Document ID:", document.id)
    print("Project ID:", document.project_id)
    print("Title:", document.title)

    if document.versions:
        version = document.versions[0]
        print("Version:", version.version_number)
        print("File name:", version.file_name)
        print("File size:", version.file_size)
        print("SHA-256:", version.file_hash)
        print("Storage key:", version.storage_key)
        print("Processing status:", version.processing_status)

finally:
    db.close()