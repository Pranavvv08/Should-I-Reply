from django.shortcuts import render
from .forms import EmailForm
from .emailanalyze import analyze_email
from .emailfetcher import fetch_recent_emails

def sample_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_id = form.cleaned_data['email']
            password = form.cleaned_data['password']

            max_emails = 5
            emails = fetch_recent_emails(email_id, password, max_emails=max_emails)

            if not emails or 'Error' in emails[0]['subject']:
                return render(request, 'analyze/result.html', {
                    'error': "Could not fetch emails. Please check your credentials or try again."
                })

            results = []
            for email in emails:
                subject = email["subject"]
                body = email["body"]
                result = analyze_email(subject, body)
                results.append({
                    "subject": subject,
                    # "body": body,
                    "summary": result["summary"],
                    "urgency": result["urgency"],
                    "reply": result["reply"],
                    "should_reply": result["reply"] != "No reply needed.",
                    "recommendation_reason": result["reply"] if result["reply"] != "No reply needed." else "This email appears to be informational or not important enough to warrant a response."
                })

            return render(request, 'analyze/result.html', {'results': results})
    else:
        form = EmailForm()

    return render(request, 'analyze/form.html', {'form': form})
