Duration: 3 hours, May 7, 2024, 10:00 PM to May 7, 2024, 1:00 AM (UTC).
Impact: The website experienced intermittent downtime, affecting 20% of users.
Root Cause: A configuration error in the database connection settings caused database connections to max out, leading to service disruption.
Timeline:

10:00 PM: Issue detected through automated monitoring alerts showing a spike in error rates.
10:05 PM: Engineering team alerted and began investigating the issue.
10:15 PM: Assumed database overload due to recent traffic increase; optimization attempts started.
10:30 PM: No improvement observed; suspicion shifted to database configuration issues.
10:45 PM: Discovered misconfigured database connection settings causing connection limit exhaustion.
11:00 PM: Increased database connection limits temporarily to restore service.
12:00 AM: Implemented permanent fix by adjusting database connection pool settings.
1:00 AM: Service fully restored, error rates back to normal levels.
Root Cause and Resolution:

The root cause was traced to a misconfiguration in the database connection settings, causing database connections to reach their limit and leading to service disruption. To resolve the issue, the database connection limits were temporarily increased to restore service, followed by a permanent fix by adjusting connection pool settings to handle increased traffic more efficiently.

Corrective and Preventative Measures:

Improvements/Fixes:
Implement automated configuration checks to detect and prevent similar misconfigurations.
Enhance monitoring to proactively identify database connection issues before they affect service.
Tasks to Address the Issue:
Conduct a thorough review of all database configuration settings to ensure they align with current traffic patterns.
Develop and document procedures for rapidly adjusting database configurations in emergency situations.
