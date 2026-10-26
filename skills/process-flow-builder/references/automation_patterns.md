# Process Flow Patterns and Automation Opportunities

## Common Automation Patterns

### Data Entry and Transfer
- Manual copying between systems → API integration, webhooks, or automation tools (Zapier, Make, n8n)
- Form completion → Auto-fill from CRM/database
- Spreadsheet updates → Real-time sync from source systems
- Document generation → Template automation with variable injection

### Communication and Notifications
- Manual emails at process stages → Automated triggered emails
- Status update messages → Slack/Teams webhooks
- Reminder sending → Calendar-based automation
- Report distribution → Scheduled automated reports

### Approval Workflows
- Manual approval requests → Approval workflow tools (ApprovalMax, Jira)
- Signature collection → DocuSign, Adobe Sign
- Budget sign-off → Automated routing based on amount thresholds
- Multi-level approvals → Sequential automated workflow

### Monitoring and Compliance
- Manual deadline tracking → Automated reminder systems
- Compliance checking → Rules-based validation
- Duplicate detection → Database constraints or deduplication scripts
- Audit trail creation → Automated logging

### Document Management
- Version control → Google Docs revision history, Git
- File organisation → Automated folder structures, naming conventions
- Access control → Permission automation based on roles
- Archival → Scheduled archive workflows

## Process Decomposition Principles

### Identifying Sub-steps
Look for:
- Sequential actions within a broader task
- Different actors involved in parts of a step
- Decision points that branch
- Iteration or loops

### Good Sub-step Example
Main step: "Process invoice for payment"
- 1.1: Verify invoice details against PO
- 1.2: Check budget availability
- 1.3: Route to appropriate approver
- 1.4: Enter into accounting system

### Owner Assignment Heuristics
- "Review" or "Approve" → Usually manager/senior role
- "Create" or "Draft" → Usually executor/team member
- "Submit" → Usually requester
- "Process" → Usually operations/finance team
- "Notify" → Usually system or admin

### Due Date Patterns
- Review/approval steps → 2-3 days after previous step
- Data entry → 1 day
- Board/senior approval → Align to meeting schedule (monthly, quarterly)
- Month-end processes → Specific dates (e.g., 5th, 10th)
- Payment processing → Fixed calendar (e.g., 15th and 30th)

### People Informed Patterns
- Process initiator → Informed at completion
- Budget owner → Informed of spending
- Compliance roles → Informed of regulatory steps
- Next step owner → Informed when their step is ready
- Senior management → Informed of high-value or high-risk items
