def clean_multiline(text: str) -> str:
    return '\n'.join(line.lstrip() for line in text.splitlines()).strip('\n')

CUSTOMER_SUPPORT_TEST_SET_NAME = 'Customer Support Test Set'
CUSTOMER_SUPPORT_TEST_SET_DESCRIPTION = 'Customer Support Test Set'
CUSTOMER_SUPPORT_TEST_CASES_RAW = [
    {
        'name': 'TC_001',
        'scenario': """
        After scheduling a closing you want to find the notary's contact details. Ask where exactly they are displayed.
        """,
        'scenario_survey': """
        After scheduling a closing (loan signing process) you want to find the notary's contact details. Ask where exactly they are displayed.
        """,
        'difficulty': 'Easy'
    },
    {
        'name': 'TC_002',
        'scenario': """
        You already activated your account but forgot your password. You want help using the 'Forgot Password' flow, using the temporary password email, and then creating a new password.
        """,
        'scenario_survey': """
        You already activated your account but forgot your password. You want help using the 'Forgot Password' flow, using the temporary password email, and then creating a new password.
        """,
        'difficulty': 'Easy'
    },
    {
        'name': 'TC_003',
        'scenario': """
        Inside a loan file you want to locate the banner details, find the Instructions section, and upload additional documents.
        """,
        'scenario_survey': """
        Inside a loan file you want to locate the banner details, find the Instructions section, and upload additional documents.
        """,
        'difficulty': 'Easy'
    },
    {
        'name': 'TC_005',
        'scenario': """
        You need to understand RON scheduling: ask who sets the RON appointment, where to see the Signing Room, and when confirmed details appear.
        """,
        'scenario_survey': """
        You need to understand how RON scheduling works (Remote Online Notarization — where the signing is done fully online). You want to ask who is responsible for setting the RON appointment, where you can see the Signing Room, and when the confirmed details — like date, time, and notary info — will appear.
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_006',
        'scenario': """
        You want to schedule a traditional/hybrid closing using borrower preferences, choose a time slot, set notarization, and confirm if the date can be changed once scheduled.
        """,
        'scenario_survey': """
        You want to schedule a traditional or hybrid closing (signing done fully on paper, or partly online and partly on paper). You need to use the borrower's preferences, pick a time slot, choose the notarization method, and confirm whether the date can be changed after it's scheduled.
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_007',
        'scenario': """
        Borrower hasn't finished eSign yet. You uploaded ink-signed docs and saw a prompt. Clarify whether the eSign docs are included or if you need to remind the borrower.
        """,
        'scenario_survey': """
        The borrower hasn't finished their eSign (electronic signing) yet. You already uploaded the ink-signed paper documents and then saw a prompt. You want to clarify whether the eSign documents are already included, or if you still need to remind the borrower to complete them.
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_004',
        'scenario': """
        You're new to the Pipeline View: want to filter for today's closings with pending eSign, sort by Closing Date, and search by address.
        """,
        'scenario_survey': """
        You are new to the Pipeline View (the list of loans you're working on). You want to know how to filter for today's closings (loan signing processes) that still have pending eSign (electronic signing) tasks, how to sort the list by Closing Date, and how to search using a property address.
        """,
        'difficulty': 'Easy'
    },
    {
        'name': 'TC_011',
        'scenario': """
        You are a notary who has just been sent a closing package by a settlement agent. You need to activate your Notary Workspace account, choose MFA method, complete your profile, and access documents.
        """,
        'scenario_survey': """
        You are a notary, and a settlement agent has just shared a closing package (the set of loan documents) with you. You need to activate your Notary Workspace account, pick a Multi-Factor Authentication (MFA) method for security, finish filling out your profile, and then access the documents.
        """,
        'difficulty': 'Hard'
    },
    {
        'name': 'TC_008',
        'scenario': """
        You need to activate your account, then immediately schedule a closing, and finally share the closing package with another agent.
        """,
        'scenario_survey': """
        You need to activate your account, then immediately schedule a closing (loan signing process), and finally share the closing package with another agent.
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_009',
        'scenario': """
        You want to share a closing with both an attorney and a notary, but one has no account and the other already does. Afterward you also want to confirm borrower-preferred scheduling slots.
        """,
        'scenario_survey': """
        You want to share a closing (loan signing process) with both an attorney and a notary, but one has no account and the other already does. Afterward you also want to confirm borrower-preferred scheduling slots.
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_012',
        'scenario': """
        You must upload ink-signed docs, handle the prompt because eSign is incomplete, and then find notary contact info to remind them.
        """,
        'scenario_survey': """
        You need to upload the ink-signed paper documents. When you do, the system shows a message because the borrower hasn't finished their eSign (electronic signing). You want to know how to respond — whether to mark the eSign documents as already included or to remind the borrower to complete them. You also need to find the notary's contact information so you can follow up with them.
        """,
        'difficulty': 'Hard'
    },
    {
        'name': 'TC_013',
        'scenario': """
        You have a list of 4 very specific feature requests, framed as questions. 1. "How do I set up a rule to auto-assign all loans from 'Lender X' to my 'High-Value' team?" 2. "Where is the audit log to see which team member downloaded a closing package?" 3. "How do I generate a report of all my closings from last quarter?" 4. "How do I reset my password?".
        """,
        'scenario_survey': """
        You have a list of 4 very specific feature requests, framed as questions. 1. "How do I set up a rule to auto-assign all loans from 'Lender X' to my 'High-Value' team?" 2. "Where is the audit log to see which team member downloaded a closing package?" 3. "How do I generate a report of all my closings from last quarter?" 4. "How do I reset my password?".
        """,
        'difficulty': 'Hard'
    },
    {
        'name': 'TC_010',
        'scenario': """
        You need to upload a 50MB PDF as a trailing document. Is there a file size limit? While you check that, can you also tell me where in the UI I can see the loan's interest rate? And finally, who gets notified when I upload this trailing document?
        """,
        'scenario_survey': """
        You need to upload a 50MB PDF as a trailing document. Is there a file size limit? While you check that, can you also tell me where in the UI I can see the loan's interest rate? And finally, who gets notified when I upload this trailing document?
        """,
        'difficulty': 'Medium'
    },
    {
        'name': 'TC_014',
        'scenario': """
        You have a bad connection that cuts out occasionally. You need to reset your password, but the email isn't arriving. You also need to upload a document for a closing that is happening in 10 minutes, but the upload button isn't working. Mid-call, you must interrupt the agent and ask if ***** offers services in Canada.
        """,
        'scenario_survey': """
        You have a bad connection that cuts out occasionally. You need to reset your password, but the email isn't arriving. You also need to upload a document for a closing (loan signing process) that is happening in 10 minutes, but the upload button isn't working. During the call, you must interrupt the agent and ask if ***** offers services in Canada.
        """,
        'difficulty': 'Hard'
    },
    {
        'name': 'TC_015',
        'scenario': """
        You are a settlement agent. You shared a closing with a notary. The notary claims they completed their profile but you still can't see their phone number in the Contacts tab. You also need to know if you can set a default notary for all your closings.
        """,
        'scenario_survey': """
        You are a settlement agent. You shared a closing (loan signing process) with a notary. The notary claims they completed their profile in the application but you still can't see their phone number in the Contacts tab. You also need to know if you can set a default notary for all your closings.
        """,
        'difficulty': 'Hard'
    },
]
CUSTOMER_SUPPORT_TEST_CASES = [
    {
        'name': ctccr['name'],
        'scenario': clean_multiline(ctccr['scenario']),
        'scenario_survey': clean_multiline(ctccr['scenario_survey']),
        'difficulty': ctccr['difficulty']
    }
    for ctccr in CUSTOMER_SUPPORT_TEST_CASES_RAW
]
