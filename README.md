# PropertyGuard

## AI-Assisted Property Compliance & Risk Assessment Platform

PropertyGuard is a web-based platform designed to help users assess residential properties for compliance and risk using property documents, AI-assisted document analysis, deterministic regulatory rules, official verification, and machine learning.

The initial target geography is **Telangana, India**, with the architecture designed to support expansion to additional Indian states.

---

## Features

### Builder

- Builder registration and verification
- RERA/company/project verification
- Create and manage property projects
- Project approval and versioning
- Upload and manage property documents
- Document versioning and duplicate detection
- OCR and AI-assisted document extraction
- View compliance findings
- Resolve findings with supporting evidence
- Monitor property risk and compliance
- Receive document expiry and workflow notifications
- Respond to Buyer requests
- Generate assessment reports

### Buyer

- Search properties without login
- View public property summaries
- Authenticated access to protected property information
- View authorized compliance and risk information
- Access permitted property documents
- Request additional information
- Report suspicious documents or information
- Upload documents for an unlisted property
- Create a temporary private assessment
- Download assessment reports
- Explicitly share private assessments with Builders

### Admin

- Admin dashboard
- Builder verification
- Project approval/rejection
- Document and AI/OCR review
- Compliance rule management
- RERA/official verification
- Finding management
- Risk management
- Regulatory update management
- User and visibility management
- Audit logs
- System health monitoring

### Super Admin

- All authorized Admin functionality
- Admin account management
- High-privilege configuration and authority operations

---

## System Architecture

PropertyGuard follows a **layered and modular architecture**.

```text
                         PROPERTYGUARD
                              |
                    +---------+---------+
                    |                   |
              React Frontend       FastAPI Backend
                    |                   |
                    |            +------+------+
                    |            |             |
                 REST API    Application    WebSocket
                              Services
                                  |
             +--------------------+--------------------+
             |          |           |        |          |
           Auth     Projects    Documents  Reports   Audit
                                  |
                           Background Jobs
                                  |
                           Celery + Redis
                                  |
                    +-------------+-------------+
                    |                           |
                  OCR                          AI
             PyMuPDF/PaddleOCR          AIService
                                             |
                                  +----------+----------+
                                  |                     |
                               Gemini                 Ollama
                                  |
                           Evidence & Confidence
                                  |
                    +-------------+-------------+
                    |                           |
             Discrepancy Engine          Compliance Engine
                    |                           |
                    +-------------+-------------+
                                  |
                            Risk Engine
                                  |
                    +-------------+-------------+
                    |                           |
             Deterministic Risk            ML Risk
                                           Random Forest
                    |                           |
                    +-------------+-------------+
                                  |
                       PropertyGuard Risk
                          Assessment Score
                                  |
                    +-------------+-------------+
                    |                           |
                 PostgreSQL                   MinIO# PropertyGuard




SOFTWARE DESIGN
FIGMA LINK: - https://www.figma.com/design/M1B8JrCvubxdWri4eA3Sot/Mokshith-Reddy-s-team-library?node-id=3314-2&t=6DxSbyCToAG4ZJPx-1
