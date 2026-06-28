REVIEWERS = [
    {
        "id": "r1",
        "name": "Maya Chen",
        "title": "Senior Counsel",
        "email": "maya@legalco.com",
    },
    {
        "id": "r2",
        "name": "James Park",
        "title": "Contract Manager",
        "email": "james@legalco.com",
    },
    {
        "id": "r3",
        "name": "Priya Sharma",
        "title": "General Counsel",
        "email": "priya@legalco.com",
    },
]

CONTRACTS = {
    "1": {
        "id": "1",
        "filename": "acme_nda.pdf",
        "type": "NDA",
        "counterparty": "Acme Corp",
        "risk_score": 82,
        "risk_level": "High",
        "status": "Pending Review",
        "uploaded_at": "2026-06-25T14:30:00",
        "uploaded_by": "sarah@company.com",
        "clause_count": 24,
        "redlines": [
            {
                "id": "r1-1",
                "clause_title": "Automatic Renewal",
                "original": (
                    "This Agreement shall remain in effect for a period of five (5) years from the "
                    "Effective Date, and shall automatically renew for successive one (1) year periods "
                    "unless either party provides written notice of termination at least ninety (90) "
                    "days prior to the expiration of the then-current term."
                ),
                "suggested": (
                    "This Agreement shall remain in effect for a period of two (2) years from the "
                    "Effective Date. This Agreement shall NOT automatically renew without express "
                    "written consent from both parties at least thirty (30) days prior to expiration."
                ),
                "rationale": (
                    "Auto-renewal with a 90-day cancellation window creates significant lock-in risk. "
                    "The 5-year initial term is also above market. Recommend 2-year term with opt-in renewal."
                ),
                "severity": "Critical",
                "accepted": False,
            },
            {
                "id": "r1-2",
                "clause_title": "IP Ownership",
                "original": (
                    "Any and all work product, inventions, discoveries, improvements, or other "
                    "intellectual property created by the Receiving Party using the Disclosing Party's "
                    "Confidential Information shall be the exclusive property of the Disclosing Party."
                ),
                "suggested": (
                    "Any work product created solely and directly from the Disclosing Party's "
                    "Confidential Information shall be the exclusive property of the Disclosing Party. "
                    "Pre-existing IP of the Receiving Party and independently developed IP shall remain "
                    "the exclusive property of the Receiving Party."
                ),
                "rationale": (
                    "This clause as written claims ownership of any IP the Receiving Party develops "
                    "while using Disclosing Party's information, even tangentially. This is overbroad "
                    "and could sweep in unrelated R&D. Narrowing to direct derivatives only."
                ),
                "severity": "High",
                "accepted": False,
            },
            {
                "id": "r1-3",
                "clause_title": "Liability Cap",
                "original": (
                    "In no event shall either party's aggregate liability under this Agreement exceed "
                    "ten million dollars ($10,000,000). This limitation shall apply regardless of the "
                    "cause of action or the form of action."
                ),
                "suggested": (
                    "In no event shall either party's aggregate liability under this Agreement exceed "
                    "the greater of (i) five hundred thousand dollars ($500,000) or (ii) the fees paid "
                    "by the Receiving Party in the twelve (12) months preceding the claim."
                ),
                "rationale": (
                    "$10M liability cap is unusually high for a mutual NDA with no commercial transaction. "
                    "Market standard for NDAs is either $500K or fees-paid-based. Recommend reducing."
                ),
                "severity": "High",
                "accepted": False,
            },
        ],
        "flagged_clauses": [
            {
                "id": "f1-1",
                "clause_title": "Automatic Renewal",
                "severity": "Critical",
                "category": "Auto-renewal",
                "excerpt": "…shall automatically renew for successive one (1) year periods unless "
                "either party provides written notice…90 days prior…",
                "rationale": "90-day cancellation window combined with auto-renewal creates lock-in. "
                "5-year initial term is above market for NDAs.",
            },
            {
                "id": "f1-2",
                "clause_title": "IP Ownership Sweep",
                "severity": "High",
                "category": "IP Ownership",
                "excerpt": "…intellectual property created by the Receiving Party using the Disclosing "
                "Party's Confidential Information shall be the exclusive property…",
                "rationale": "Overbroad IP assignment could claim ownership of independently developed work.",
            },
            {
                "id": "f1-3",
                "clause_title": "Uncapped Liability ($10M)",
                "severity": "High",
                "category": "Liability",
                "excerpt": "…aggregate liability…shall not exceed ten million dollars ($10,000,000)…",
                "rationale": "Above-market liability cap for a mutual NDA with no underlying commercial deal.",
            },
        ],
        "audit_trail": [
            {
                "timestamp": "2026-06-25T14:30:00",
                "action": "Uploaded",
                "actor": "sarah@company.com",
                "detail": "acme_nda.pdf uploaded via web interface",
            },
            {
                "timestamp": "2026-06-25T14:31:45",
                "action": "AI Review Complete",
                "actor": "LegalAI",
                "detail": "Risk score 82/100 · 3 redlines · 3 flagged clauses",
            },
        ],
        "full_text_paragraphs": [
            {
                "id": "p1",
                "number": "1.",
                "title": "Definitions",
                "text": (
                    '"Confidential Information" means any non-public information that relates to the '
                    "actual or anticipated business and research and development of the Disclosing "
                    "Party, including but not limited to financial data, technical plans, product "
                    "roadmaps, customer lists, and business strategies, whether communicated orally "
                    "or in documentary form."
                ),
                "flagged": False,
            },
            {
                "id": "p2",
                "number": "2.",
                "title": "Confidentiality Obligations",
                "text": (
                    "The Receiving Party agrees to hold the Confidential Information of the Disclosing "
                    "Party in strict confidence and to take all reasonable precautions to protect such "
                    "Confidential Information. The Receiving Party shall not disclose any Confidential "
                    "Information to any third party without the prior written consent of the Disclosing Party."
                ),
                "flagged": False,
            },
            {
                "id": "p3",
                "number": "3.",
                "title": "IP Ownership",
                "text": (
                    "Any and all work product, inventions, discoveries, improvements, or other "
                    "intellectual property created by the Receiving Party using the Disclosing Party's "
                    "Confidential Information shall be the exclusive property of the Disclosing Party."
                ),
                "flagged": True,
                "flag_severity": "High",
                "redline_id": "r1-2",
            },
            {
                "id": "p4",
                "number": "4.",
                "title": "Term and Automatic Renewal",
                "text": (
                    "This Agreement shall remain in effect for a period of five (5) years from the "
                    "Effective Date, and shall automatically renew for successive one (1) year periods "
                    "unless either party provides written notice of termination at least ninety (90) "
                    "days prior to the expiration of the then-current term."
                ),
                "flagged": True,
                "flag_severity": "Critical",
                "redline_id": "r1-1",
            },
            {
                "id": "p5",
                "number": "5.",
                "title": "Limitation of Liability",
                "text": (
                    "In no event shall either party's aggregate liability under this Agreement exceed "
                    "ten million dollars ($10,000,000). This limitation shall apply regardless of the "
                    "cause of action or the form of action."
                ),
                "flagged": True,
                "flag_severity": "High",
                "redline_id": "r1-3",
            },
            {
                "id": "p6",
                "number": "6.",
                "title": "Governing Law",
                "text": (
                    "This Agreement shall be governed by and construed in accordance with the laws of "
                    "the State of Delaware, without regard to its conflict of law provisions. Any "
                    "disputes arising under this Agreement shall be resolved in the courts of the "
                    "State of Delaware."
                ),
                "flagged": False,
            },
        ],
    },
    "2": {
        "id": "2",
        "filename": "vendor_saas_agreement.pdf",
        "type": "Vendor",
        "counterparty": "Stripe Inc.",
        "risk_score": 45,
        "risk_level": "Medium",
        "status": "Pending Review",
        "uploaded_at": "2026-06-26T09:15:00",
        "uploaded_by": "mike@company.com",
        "clause_count": 38,
        "redlines": [
            {
                "id": "r2-1",
                "clause_title": "Data Processing & Portability",
                "original": (
                    "Upon termination of this Agreement, Stripe shall have no obligation to retain "
                    "or provide Customer Data and may delete all Customer Data within 30 days of termination."
                ),
                "suggested": (
                    "Upon termination of this Agreement, Stripe shall provide Customer with an export "
                    "of all Customer Data in machine-readable format within 15 days of termination request. "
                    "Stripe shall retain Customer Data for a minimum of 60 days post-termination to allow "
                    "for data migration."
                ),
                "rationale": (
                    "Current clause gives Stripe unilateral right to delete customer data with no export "
                    "obligation. This creates vendor lock-in and may violate data portability obligations "
                    "under GDPR/CCPA. Request data export SLA."
                ),
                "severity": "Medium",
                "accepted": False,
            },
        ],
        "flagged_clauses": [
            {
                "id": "f2-1",
                "clause_title": "Data Deletion on Termination",
                "severity": "Medium",
                "category": "Data Rights",
                "excerpt": "…Stripe shall have no obligation to retain or provide Customer Data "
                "and may delete all Customer Data within 30 days…",
                "rationale": "No data export obligation on termination. May conflict with GDPR data portability rights.",
            },
        ],
        "audit_trail": [
            {
                "timestamp": "2026-06-26T09:15:00",
                "action": "Uploaded",
                "actor": "mike@company.com",
                "detail": "vendor_saas_agreement.pdf uploaded via web interface",
            },
            {
                "timestamp": "2026-06-26T09:16:20",
                "action": "AI Review Complete",
                "actor": "LegalAI",
                "detail": "Risk score 45/100 · 1 redline · 1 flagged clause",
            },
        ],
        "full_text_paragraphs": [
            {
                "id": "p1",
                "number": "1.",
                "title": "Services",
                "text": (
                    "Stripe agrees to provide the payment processing services described in the applicable "
                    "Order Form(s) (the 'Services'). Stripe will use commercially reasonable efforts to "
                    "make the Services available 99.9% of the time in any given calendar month."
                ),
                "flagged": False,
            },
            {
                "id": "p2",
                "number": "2.",
                "title": "Data Processing",
                "text": (
                    "Upon termination of this Agreement, Stripe shall have no obligation to retain "
                    "or provide Customer Data and may delete all Customer Data within 30 days of termination."
                ),
                "flagged": True,
                "flag_severity": "Medium",
                "redline_id": "r2-1",
            },
        ],
    },
    "3": {
        "id": "3",
        "filename": "mutual_nda_techco.pdf",
        "type": "NDA",
        "counterparty": "TechCo Solutions",
        "risk_score": 28,
        "risk_level": "Low",
        "status": "Approved",
        "uploaded_at": "2026-06-20T11:00:00",
        "uploaded_by": "sarah@company.com",
        "clause_count": 18,
        "redlines": [],
        "flagged_clauses": [],
        "audit_trail": [
            {
                "timestamp": "2026-06-20T11:00:00",
                "action": "Uploaded",
                "actor": "sarah@company.com",
                "detail": "mutual_nda_techco.pdf uploaded via web interface",
            },
            {
                "timestamp": "2026-06-20T11:01:10",
                "action": "AI Review Complete",
                "actor": "LegalAI",
                "detail": "Risk score 28/100 · 0 redlines · 0 flagged clauses",
            },
            {
                "timestamp": "2026-06-20T14:30:00",
                "action": "Approved",
                "actor": "sarah@company.com",
                "detail": "Contract approved — standard mutual NDA terms",
            },
        ],
        "full_text_paragraphs": [],
    },
    "4": {
        "id": "4",
        "filename": "supplier_agreement.pdf",
        "type": "Vendor",
        "counterparty": "Amazon Web Services",
        "risk_score": 91,
        "risk_level": "Critical",
        "status": "Escalated",
        "uploaded_at": "2026-06-27T08:45:00",
        "uploaded_by": "mike@company.com",
        "clause_count": 52,
        "redlines": [
            {
                "id": "r4-1",
                "clause_title": "Unilateral Modification Rights",
                "original": (
                    "AWS reserves the right to modify these terms at any time by posting revised terms "
                    "on the AWS website. Your continued use of the Services after such posting constitutes "
                    "your acceptance of the revised terms."
                ),
                "suggested": (
                    "AWS may not modify these terms without providing Customer with at least 30 days "
                    "written notice via email. Customer shall have the right to terminate the Agreement "
                    "without penalty within such 30-day notice period if Customer does not accept the "
                    "proposed modifications."
                ),
                "rationale": (
                    "Unilateral right to modify terms via website posting with no notice is one-sided "
                    "and may render the contract illusory. Require 30-day advance notice and termination "
                    "rights for material changes."
                ),
                "severity": "Critical",
                "accepted": False,
            },
            {
                "id": "r4-2",
                "clause_title": "Indemnification — Uncapped",
                "original": (
                    "Customer shall indemnify, defend, and hold harmless AWS and its affiliates from "
                    "any and all claims, damages, losses, costs, and expenses (including reasonable "
                    "attorneys' fees) arising out of or related to Customer's use of the Services."
                ),
                "suggested": (
                    "Customer shall indemnify AWS from third-party claims arising out of Customer's "
                    "material breach of this Agreement or Customer's gross negligence, limited to direct "
                    "damages not exceeding the fees paid by Customer in the prior 12 months."
                ),
                "rationale": (
                    "Uncapped, one-sided indemnification with 'arising out of or related to' scope is "
                    "overbroad. Should be mutual, limited to gross negligence/willful misconduct, and "
                    "capped at fees paid."
                ),
                "severity": "Critical",
                "accepted": False,
            },
        ],
        "flagged_clauses": [
            {
                "id": "f4-1",
                "clause_title": "Unilateral Modification Rights",
                "severity": "Critical",
                "category": "Contract Control",
                "excerpt": "…reserves the right to modify these terms at any time by posting revised "
                "terms on the AWS website…",
                "rationale": "Allows unilateral material changes with no notice. Makes contract terms unpredictable.",
            },
            {
                "id": "f4-2",
                "clause_title": "Uncapped One-Sided Indemnification",
                "severity": "Critical",
                "category": "Indemnification",
                "excerpt": "…indemnify, defend, and hold harmless AWS…any and all claims, damages, "
                "losses, costs, and expenses…",
                "rationale": "Uncapped indemnification obligation with unlimited scope. Significant financial exposure.",
            },
        ],
        "audit_trail": [
            {
                "timestamp": "2026-06-27T08:45:00",
                "action": "Uploaded",
                "actor": "mike@company.com",
                "detail": "supplier_agreement.pdf uploaded via web interface",
            },
            {
                "timestamp": "2026-06-27T08:46:30",
                "action": "AI Review Complete",
                "actor": "LegalAI",
                "detail": "Risk score 91/100 · 2 redlines · 2 flagged clauses",
            },
            {
                "timestamp": "2026-06-27T09:00:00",
                "action": "Escalated",
                "actor": "mike@company.com",
                "detail": "Escalated to Maya Chen (Senior Counsel) — Critical risk clauses require legal review",
            },
        ],
        "full_text_paragraphs": [
            {
                "id": "p1",
                "number": "1.",
                "title": "Modification Rights",
                "text": (
                    "AWS reserves the right to modify these terms at any time by posting revised terms "
                    "on the AWS website. Your continued use of the Services after such posting constitutes "
                    "your acceptance of the revised terms."
                ),
                "flagged": True,
                "flag_severity": "Critical",
                "redline_id": "r4-1",
            },
            {
                "id": "p2",
                "number": "2.",
                "title": "Customer Indemnification",
                "text": (
                    "Customer shall indemnify, defend, and hold harmless AWS and its affiliates from "
                    "any and all claims, damages, losses, costs, and expenses (including reasonable "
                    "attorneys' fees) arising out of or related to Customer's use of the Services."
                ),
                "flagged": True,
                "flag_severity": "Critical",
                "redline_id": "r4-2",
            },
        ],
    },
    "5": {
        "id": "5",
        "filename": "consulting_nda.pdf",
        "type": "NDA",
        "counterparty": "Deloitte LLP",
        "risk_score": 55,
        "risk_level": "Medium",
        "status": "Pending Review",
        "uploaded_at": "2026-06-28T10:00:00",
        "uploaded_by": "lisa@company.com",
        "clause_count": 21,
        "redlines": [
            {
                "id": "r5-1",
                "clause_title": "Non-Solicitation Scope",
                "original": (
                    "For a period of two (2) years following the termination of this Agreement, "
                    "neither party shall directly or indirectly solicit, recruit, or hire any employee "
                    "or contractor of the other party."
                ),
                "suggested": (
                    "For a period of one (1) year following the termination of this Agreement, "
                    "neither party shall directly solicit employees of the other party who were "
                    "directly involved in the engagement described herein."
                ),
                "rationale": (
                    "2-year mutual non-solicitation covering all employees and contractors is broad. "
                    "Market standard for consulting NDAs is 1 year, limited to directly involved personnel."
                ),
                "severity": "Medium",
                "accepted": False,
            },
        ],
        "flagged_clauses": [
            {
                "id": "f5-1",
                "clause_title": "Broad Non-Solicitation",
                "severity": "Medium",
                "category": "Non-Solicitation",
                "excerpt": "…shall directly or indirectly solicit, recruit, or hire any employee "
                "or contractor…for a period of two (2) years…",
                "rationale": "Broad 2-year non-solicitation may restrict normal hiring. Narrower scope recommended.",
            },
        ],
        "audit_trail": [
            {
                "timestamp": "2026-06-28T10:00:00",
                "action": "Uploaded",
                "actor": "lisa@company.com",
                "detail": "consulting_nda.pdf uploaded via web interface",
            },
            {
                "timestamp": "2026-06-28T10:01:05",
                "action": "AI Review Complete",
                "actor": "LegalAI",
                "detail": "Risk score 55/100 · 1 redline · 1 flagged clause",
            },
        ],
        "full_text_paragraphs": [
            {
                "id": "p1",
                "number": "1.",
                "title": "Non-Solicitation",
                "text": (
                    "For a period of two (2) years following the termination of this Agreement, "
                    "neither party shall directly or indirectly solicit, recruit, or hire any employee "
                    "or contractor of the other party."
                ),
                "flagged": True,
                "flag_severity": "Medium",
                "redline_id": "r5-1",
            },
        ],
    },
}
