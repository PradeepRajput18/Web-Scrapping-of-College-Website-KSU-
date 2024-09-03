import matplotlib.pyplot as plt

# Data for email frequencies
email_labels = ['ksugrad@kennesaw.edu', 'ksutesting@kennesaw.edu', 'ccseinternship@kennesaw.edu',
                'gteixeir@kennesaw.edu', 'radam108@kennesaw.edu', 'jrb4358@kennesaw.edu',
                'cbonapar@kennesaw.edu', 'jhamsnes@kennesaw.edu', 'bwalk138@kennesaw.edu',
                'csuarezv@kennesaw.edu']
email_counts = [33, 18, 16, 14, 14, 14, 14, 14, 14, 14]

# Data for word frequencies before removing stopwords
terms_before = ['', 'and', 'the', 'to', 'of', 'in', 'for', 'kennesaw', 'a', 'students',
                'campus', 'university', 'on', 'state', 'ksu', 'community', 'faculty', 'research',
                'student', 'share', 'marietta', 'alumni', 'resources', 'information', '2024',
                'search', 'with', 'is', 'all', 'or']
freq_before = [19003, 12885, 12734, 10087, 9539, 6778, 6123, 6090, 6047, 5741, 4923, 4616, 
               4308, 4255, 4104, 3059, 3013, 2794, 2784, 2755, 2709, 2648, 2636, 2620, 
               2555, 2551, 2500, 2474, 2401, 2393]

# Data for word frequencies after removing stopwords
terms_after = ['kennesaw', 'state', 'university', 'georgia', 'skip', 'main', 'navigation',
               'content', 'footer', 'apply', 'visit', 'give', 'calendar', 'resources', 
               'current', 'students', 'online', 'faculty', 'staff', 'parents', 'family',
               'alumni', 'friends', 'community', 'business', 'menu', 'ksu', 'academics',
               'admissions', 'student']
freq_after = [1] * 30  # Since each term after removing stopwords appears 1 time

# Plotting the email frequencies
plt.figure(figsize=(10, 6))
plt.barh(email_labels, email_counts, color='skyblue')
plt.xlabel('Frequency')
plt.title('Top 10 Most Frequent Email Addresses')
plt.gca().invert_yaxis()  # Highest frequency at the top
plt.show()

# Plotting the word frequencies before removing stopwords
plt.figure(figsize=(12, 8))
plt.barh(terms_before, freq_before, color='lightgreen')
plt.xlabel('Frequency')
plt.title('Top 30 Most Common Words (Before Removing Stopwords)')
plt.gca().invert_yaxis()
plt.show()

# Plotting the word frequencies after removing stopwords
plt.figure(figsize=(12, 8))
plt.barh(terms_after, freq_after, color='salmon')
plt.xlabel('Frequency')
plt.title('Top 30 Most Common Words (After Removing Stopwords)')
plt.gca().invert_yaxis()
plt.show()
