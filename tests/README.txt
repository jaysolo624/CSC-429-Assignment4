Test 1: 

input: ['budget_high', 'portable', 'long_battery'] → Expected: recommend:premium_ultrabook

Is your budget high? (y/n): y
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
Is this for office use? (y/n): n
Is this for gaming? (y/n): n
Is this for creative work? (y/n): n
Do you prefer to use Windows? (y/n): n
Do you prefer to use MacOS? (y/n): n
Do you prefer to use Linux? (y/n): n
Is AI acceleration important? (y/n): n
Do you want a large screen? (y/n): n
Do you travel often? (y/n): n
Here's some recommendations: 
> premium_ultrabook
Specs to look for: 
Reasonings
> Explanation: derived from rule 'Premium Ultrabook'


Test 2: 

input: ['budget_high', 'portable', 'long_battery', 'creative_work', 'pref_os_windows', large_screen'] → Expected: recommend:premium_ultrabook, spec:display_15_plus_color_accurate, spec:ram_16_plus

Is your budget high? (y/n): y
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
Is this for office use? (y/n): n
Is this for gaming? (y/n): n
Is this for creative work? (y/n): y
Do you prefer to use Windows? (y/n): y
Is AI acceleration important? (y/n): n
Do you want a large screen? (y/n): y
Do you travel often? (y/n): n
Here's some recommendations: 
> premium_ultrabook
Specs to look for: 
> display_15_plus_color_accurate
> ram_16_plus
Reasonings
> Explanation: derived from rule 'Premium Ultrabook'
> Explanation: derived from rule 'Portable Creative Work'
> Explanation: derived from rule 'Display Creative Work'


Test 3:

input: [] → Expected: No recommendations or specs

Is your budget high? (y/n): n
Is your budget medium? (y/n): n
Is your budget low? (y/n): n
Is portability important? (y/n): n
Do you need long battery life? (y/n): n
Is this for office use? (y/n): n
Is this for gaming? (y/n): n
Is this for creative work? (y/n): n
Do you prefer to use Windows? (y/n): n
Do you prefer to use MacOS? (y/n): n
Do you prefer to use Linux? (y/n): n
Is AI acceleration important? (y/n): n
Do you want a large screen? (y/n): n
Do you travel often? (y/n): n
Here's some recommendations: 
No recommendation could be derived from your answers.
Specs to look for: 
Reasonings


Test 4:

input: ['budget_low', 'portable', 'office_only'] → Expected: recommend:premium_ultrabook

Is your budget high? (y/n): n
Is your budget medium? (y/n): n
Is your budget low? (y/n): y
Is portability important? (y/n): y
Do you need long battery life? (y/n): n
Is this for office use? (y/n): y
Do you prefer to use Windows? (y/n): y
Is AI acceleration important? (y/n): n
Do you want a large screen? (y/n): n
Do you travel often? (y/n): n
Here's some recommendations: 
> budget_ultrabook
Specs to look for: 
Reasonings
> Explanation: derived from rule 'Budget Ultrabook'


Test 5:

input: ['budget_high', 'gaming', 'pref_os_linux', 'needs_ai_accel'] → Expected: recommend:high_end_gaming_laptop, spec:gpu_with_tensor_cores

Is your budget high? (y/n): y
Is portability important? (y/n): n
Do you need long battery life? (y/n): n
Is this for office use? (y/n): n
Is this for gaming? (y/n): y
Do you prefer to use Windows? (y/n): n
Do you prefer to use MacOS? (y/n): n
Do you prefer to use Linux? (y/n): y
Is AI acceleration important? (y/n): y
Do you want a large screen? (y/n): n
Do you travel often? (y/n): n
Here's some recommendations: 
> high_end_gaming_laptop
Specs to look for: 
> gpu_with_tensor_cores
Reasonings
> Explanation: derived from rule 'Highend Gaming Laptop'
> Explanation: derived from rule 'AI Acceleration'