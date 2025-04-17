import streamlit as st

# Set Page Config
st.set_page_config(page_title="LinkedIn Brand Assessment", page_icon=":star:", layout="wide")

# Scoring Function
def calculate_scores(responses):
    positioning = sum(1 for i in range(10) if responses[i] == "Yes") * 4  # 10 questions, total 40 points
    presence = sum(1 for i in range(10, 20) if responses[i] == "Yes") * 3.5  # 10 questions, total 35 points
    content = sum(1 for i in range(20, 30) if responses[i] == "Yes") * 3.5  # 10 questions, total 35 points
    value = sum(1 for i in range(30, 35) if responses[i] == "Yes") * 5  # 5 questions, total 25 points
    total = int(positioning + presence + content + value)
    return total, positioning, presence, content, value

# Generate dynamic insights and next steps
def get_results_analysis(total_score, role):
    if total_score >= 85:
        tone = "Industry Leader – Your Brand is Highly Optimized"
        insights = "Your LinkedIn brand is exceptionally strong. You’re positioned as an industry leader, your content resonates with your audience, and you’re likely attracting high-value opportunities consistently."
        if role == "Founder":
            next_steps = ["Leverage LinkedIn for more strategic partnerships and business deals.", "Expand your reach through media features, PR, and keynote speaking."]
        else:  # Creator
            next_steps = ["Expand your influence through speaking engagements, PR, and collaborations.", "Mentor other creators and build deeper audience loyalty."]
    elif total_score >= 70:
        tone = "Strong Presence, Needs Refinement"
        insights = "Your LinkedIn brand is strong, but gaps in positioning, network engagement, or inbound lead consistency may be limiting your full potential."
        if role == "Founder":
            next_steps = ["Strengthen business credibility markers (case studies, PR features, testimonials).", "Clarify your business offer and LinkedIn positioning."]
        else:  # Creator
            next_steps = ["Refine your personal brand messaging for better audience clarity.", "Strengthen authority signals (press features, collaborations, speaking invites)."]
    elif total_score >= 50:
        tone = "Growing, but Needs Improvement"
        insights = "Your LinkedIn brand is developing, but you’re missing out on key visibility, credibility, and inbound opportunities."
        if role == "Founder":
            next_steps = ["Optimize your profile to establish business credibility.", "Clarify your value proposition and niche expertise."]
        else:  # Creator
            next_steps = ["Optimize your profile to clearly showcase expertise and credibility.", "Clarify your niche and brand messaging."]
    else:
        tone = "Needs Significant Improvement"
        insights = "Your LinkedIn presence is underdeveloped, and you’re missing major opportunities for visibility, partnerships, and inbound leads."
        if role == "Founder":
            next_steps = ["Optimize your LinkedIn profile for credibility.", "Develop a structured LinkedIn content strategy."]
        else:  # Creator
            next_steps = ["Optimize your LinkedIn profile to improve first impressions.", "Clarify messaging to attract a relevant audience."]
    cta = "Book a Free Strategy Call" if role == "Founder" else "Join Free Skool Community"
    return tone, insights, next_steps, cta

# Enhanced feedback function for section-specific insights
def get_section_feedback(section_name, score, max_score, role):
    score_percentage = (score / max_score) * 100
    feedback = {"insight": "", "action": ""}

    if section_name == "Profile Optimization":
        if score_percentage < 50:  # Low: <20/40
            feedback["insight"] = "Your LinkedIn profile is not effectively showcasing your expertise, which may cause you to be overlooked by your target audience."
            feedback["action"] = "Revamp your headline, about section, and experience to clearly articulate your value proposition and niche expertise."
        elif score_percentage < 80:  # Medium: 20-31/40
            feedback["insight"] = "Your profile has some strong elements, but it lacks clarity or optimization to fully capture attention."
            feedback["action"] = "Refine your profile sections to align with your target audience’s needs and highlight key achievements."
        else:  # High: 32+/40
            feedback["insight"] = "Your profile is well-optimized and positions you as a credible expert in your field."
            feedback["action"] = "Leverage your strong profile to attract strategic opportunities like speaking engagements or partnerships."

    elif section_name == "Network Growth":
        if score_percentage < 50:  # Low: <17.5/35
            feedback["insight"] = "Your network is underdeveloped, limiting your visibility and opportunities on LinkedIn."
            feedback["action"] = "Actively connect with industry peers and engage with their content to build relationships."
        elif score_percentage < 80:  # Medium: 17.5-27.9/35
            feedback["insight"] = "You’ve built a decent network, but you’re not fully leveraging it for meaningful opportunities."
            feedback["action"] = "Increase engagement through comments, DMs, and LinkedIn Groups to strengthen connections."
        else:  # High: 28+/35
            feedback["insight"] = "Your network is robust, driving consistent inbound opportunities."
            feedback["action"] = "Focus on nurturing high-value connections to secure collaborations or partnerships."

    elif section_name == "Content Strategy":
        if score_percentage < 50:  # Low: <17.5/35
            feedback["insight"] = "Your content strategy is inconsistent or misaligned, reducing your audience engagement."
            feedback["action"] = "Develop a consistent posting schedule with content that aligns with your niche and audience needs."
        elif score_percentage < 80:  # Medium: 17.5-27.9/35
            feedback["insight"] = "Your content is gaining traction but lacks variety or a clear strategy to maximize impact."
            feedback["action"] = "Incorporate diverse formats (videos, carousels) and track analytics to optimize engagement."
        else:  # High: 28+/35
            feedback["insight"] = "Your content strategy is highly effective, resonating strongly with your audience."
            feedback["action"] = "Amplify your reach by pitching for media features or LinkedIn newsletters."

    elif section_name == "Personal Value Growth":
        if score_percentage < 50:  # Low: <12.5/25
            feedback["insight"] = f"As a {role}, you’re not yet capitalizing on LinkedIn to drive high-value opportunities."
            feedback["action"] = f"Clarify your unique value and create content that showcases your impact as a {role.lower()}."
        elif score_percentage < 80:  # Medium: 12.5-19.9/25
            feedback["insight"] = f"You’re starting to see value from LinkedIn, but your influence as a {role} could be stronger."
            feedback["action"] = f"Position yourself as a category leader by sharing case studies or success stories."
        else:  # High: 20+/25
            feedback["insight"] = f"Your LinkedIn presence is driving significant value, positioning you as a top {role.lower()}."
            feedback["action"] = f"Monetize your influence through premium offerings or strategic partnerships."

    return feedback

# Apply Enhanced Custom Styling
st.markdown("""
    <style>
        /* General page styling */
        .stApp {
            background-color: #F5E6E8; /* Light pink background */
            color: #4A2C2A; /* Dark brown text */
            font-family: 'Arial', sans-serif;
        }
        .header {
            background-color: #800000; /* Maroon header */
            color: #F5E6E8; /* Light pink text */
            text-align: center;
            padding: 15px;
            margin-bottom: 15px;
            font-size: 32px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .question {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #800000; /* Maroon for questions */
        }
        .role-question {
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 5px;
            color: #800000; /* Maroon for role question */
        }
        .fade-in {
            animation: fadeIn 1s forwards;
        }
        @keyframes fadeIn {
            to { opacity: 1; }
        }
        .progress-bar {
            background-color: #D3D3D3; /* Light gray */
            height: 20px;
            width: 100%;
            margin: 10px 0;
            border-radius: 5px;
        }
        .progress-fill {
            background-color: #800000; /* Maroon progress */
            height: 100%;
            border-radius: 5px;
            width: 0%;
            transition: width 0.3s ease;
        }
        .highlighted-answer {
            background-color: #FFFACD; /* Light yellow */
            padding: 2px 5px;
            color: #4A2C2A; /* Dark brown text */
            border-radius: 3px;
        }
        /* Enhanced button styling */
        .stButton > button {
            background-color: #800000; /* Maroon */
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #600000; /* Darker maroon on hover */
            cursor: pointer;
        }
        /* Custom result section styling */
        .result-section {
            background-color: #FFFFFF; /* White background for results */
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        /* Increase font size for radio options */
        .stRadio > label {
            font-size: 25px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Handle question flow with progress bar
def handle_questions(questions, next_page, section_name, total_questions_per_section, is_last_section=False):
    total_questions = len(questions)
    question_index = st.session_state.get(f"current_question_{section_name}", 0)
    section_progress = (question_index / total_questions) * 100 if question_index < total_questions else 100
    overall_progress = (st.session_state.get("questions_answered", 0) + question_index) / 35 * 100

    st.markdown(f"<h3 class='fade-in'>{section_name}</h3>", unsafe_allow_html=True)
    st.markdown("<h4 class='fade-in'>Progress Bar</h4>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='progress-bar'>
            <div class='progress-fill' style='width: {section_progress}%;'></div>
        </div>
        <p class='fade-in'>Section Progress: {int(section_progress)}% | Overall Progress: {int(overall_progress)}%</p>
    """, unsafe_allow_html=True)

    if question_index < total_questions:
        st.markdown(f"<p class='question fade-in'>{questions[question_index]}</p>", unsafe_allow_html=True)

        # Use st.radio with a non-empty label and collapsed visibility
        response_key = f"q_{question_index}_{section_name}"
        response = st.radio(
            label="Select your answer",
            options=["Yes", "No"],
            key=response_key,
            index=None if st.session_state.get(response_key) is None else ["Yes", "No"].index(st.session_state.get(response_key)),
            horizontal=True,
            label_visibility="collapsed"
        )

        if response:
            if st.button("Next" if not is_last_section or question_index < total_questions - 1 else "Finish Test"):
                st.session_state.responses.append(response)
                if question_index < total_questions - 1:
                    st.session_state[f"current_question_{section_name}"] = question_index + 1
                else:
                    if is_last_section:
                        st.session_state.page = "results_preview"  # Temporary page for "See Results"
                    else:
                        st.session_state.page = next_page
                    st.session_state[f"current_question_{section_name}"] = 0
                    st.session_state.questions_answered += total_questions_per_section
                st.rerun()
    else:
        if not is_last_section:
            if st.button("Move to Next Section"):
                st.session_state.page = next_page
                st.rerun()
        else:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Finish Test"):
                    st.session_state.page = "results_preview"
                    st.rerun()
            with col2:
                if st.button("See Results"):
                    st.session_state.page = "results"
                    st.rerun()

# Main Function
def main():
    # Initialize session state variables
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
        st.session_state.responses = []
        st.session_state.questions_answered = 0
        
        # Full set of questions from the document
        st.session_state.profile_questions = [
            "Do you have a clear plan to grow your LinkedIn personal brand over the next 12 months?",
            "Can you clearly articulate how you want people to describe you in one sentence?",
            "Do you know what areas or topics you want to be known for?",
            "Are your LinkedIn profile sections (headline, about, experience) optimized to reflect your expertise?",
            "Can you define your target audience clearly?",
            "Have you identified your audience's biggest pain points and goals?",
            "Can you clearly articulate what value your audience would get from engaging with you?",
            "Do you have a strong reason why people should follow, work with, or book you to speak?",
            "Do you feel overlooked despite having valuable expertise?",
            "Do you have notable achievements or recognitions that enhance your credibility on LinkedIn?"
        ]
        st.session_state.network_questions = [
            "Have you built a network of relevant connections within your industry?",
            "Are you regularly engaging with your network through comments and direct messages?",
            "Do you consistently receive inbound connection requests from your target audience?",
            "Are you leveraging LinkedIn features such as Groups and Events to expand your reach?",
            "Do you get inbound leads and opportunities from your LinkedIn profile?",
            "Have you been invited to speak, collaborate, or consult based on your LinkedIn presence?",
            "Are your LinkedIn DMs filled with meaningful opportunities rather than spam?",
            "Are you a part of any LinkedIn creator programs or featured as a thought leader?",
            "Do you actively seek to connect with influencers and key industry stakeholders?",
            "Have you turned LinkedIn connections into real professional opportunities?"
        ]
        st.session_state.content_questions = [
            "Do you post content on LinkedIn at least three times per week?",
            "Are your posts consistently aligned with your niche and expertise?",
            "Are you using a mix of content formats (text, video, carousels) to engage your audience?",
            "Do your posts receive meaningful engagement (likes, comments, shares)?",
            "Do you have a clear content strategy that aligns with your personal brand goals?",
            "Have you been featured in LinkedIn News or any LinkedIn newsletters?",
            "Are you using storytelling in your content to make it more relatable?",
            "Do you track your LinkedIn analytics to measure performance and improve strategy?",
            "Have you received media coverage or invitations to podcasts because of your LinkedIn content?",
            "Do you have a clear call-to-action in your content to drive engagement?"
        ]
        st.session_state.founder_questions = [
            "Do investors, potential clients, or talent reach out to you because of your LinkedIn presence?",
            "Have you used LinkedIn to successfully hire key team members?",
            "Has your LinkedIn content helped you close business deals or partnerships?",
            "Do you position yourself as a category leader in your industry?",
            "Have you been featured in industry reports, conferences, or VC discussions due to your LinkedIn presence?"
        ]
        st.session_state.creator_questions = [
            "Do brands or businesses reach out to you for sponsorships or collaborations?",
            "Have you built a community that actively engages with your content?",
            "Have you successfully monetized your LinkedIn presence (courses, paid newsletters, coaching, etc.)?",
            "Do you have a personal brand that allows you to charge premium rates for your work?",
            "Do people recognize you as a go-to expert in your niche?"
        ]

    # Welcome Page
    if st.session_state.page == "welcome":
        st.markdown("<div class='header'><h2>LinkedIn Brand Health Check</h2></div>", unsafe_allow_html=True)
        st.markdown("""
            <h3 class='fade-in'>Hi! I know what brings you here today.</h3>
            <p class='fade-in'>Let's start with your LinkedIn Brand Health Check-up!</p>
        """, unsafe_allow_html=True)
        if st.button("Begin Assessment"):
            st.session_state.page = "role_selection"
            st.rerun()

    # Role Selection
    elif st.session_state.page == "role_selection":
        st.markdown("<div class='header'><h2>LinkedIn Brand Health Check</h2></div>", unsafe_allow_html=True)
        st.markdown("<h3 class='role-question fade-in'>Who Are You?</h3>", unsafe_allow_html=True)
        st.markdown("<p class='fade-in' style='margin-bottom: 5px;'>Select your role:</p>", unsafe_allow_html=True)

        # Use st.radio with a non-empty label and collapsed visibility
        role_key = "role_selection"
        role = st.radio(
            label="Select your role",
            options=["Founder", "Creator"],
            key=role_key,
            index=None if st.session_state.get(role_key) is None else ["Founder", "Creator"].index(st.session_state.get(role_key)),
            horizontal=True,
            label_visibility="collapsed"
        )

        if role:
            if st.button("Next"):
                st.session_state.role = role
                st.session_state.page = "profile_optimization"
                st.rerun()

    # Profile Optimization Questions
    elif st.session_state.page == "profile_optimization":
        handle_questions(st.session_state.profile_questions, "network_growth", "Profile Optimization", 10, is_last_section=False)

    # Network Growth Questions
    elif st.session_state.page == "network_growth":
        handle_questions(st.session_state.network_questions, "content_strategy", "Network Growth", 10, is_last_section=False)

    # Content Strategy Questions
    elif st.session_state.page == "content_strategy":
        handle_questions(st.session_state.content_questions, "personal_value_growth", "Content Strategy", 10, is_last_section=False)

    # Personal Value Growth Questions
    elif st.session_state.page == "personal_value_growth":
        questions = st.session_state.founder_questions if st.session_state.role == "Founder" else st.session_state.creator_questions
        handle_questions(questions, "results", "Personal Value Growth", 5, is_last_section=True)

    # Results Preview (Temporary page for "See Results" button)
    elif st.session_state.page == "results_preview":
        st.markdown("<div class='header'><h2>Results Preview</h2></div>", unsafe_allow_html=True)
        st.markdown("<p class='fade-in'>Test completed! Click below to see your results.</p>", unsafe_allow_html=True)
        if st.button("See Results"):
            st.session_state.page = "results"
            st.rerun()

    # Updated Results Page
    elif st.session_state.page == "results":
        st.markdown("<div class='header'><h2>Your LinkedIn Personal Brand Scoreboard</h2></div>", unsafe_allow_html=True)
        total_score, positioning_score, presence_score, content_score, profit_score = calculate_scores(st.session_state.responses)
        tone, insights, next_steps, cta = get_results_analysis(total_score, st.session_state.role)
        ranking = total_score  # Using direct score as per original logic

        # Overall Score and Summary
        st.markdown(f"""
            <div class='result-section'>
                <h3 class='fade-in'>🏆 Your LinkedIn Personal Brand Score: {total_score}/100</h3>
                <p class='fade-in'>(Ranking: You scored higher than {ranking}% of {st.session_state.role}s who took this assessment.)</p>
                <p class='fade-in'><strong>{tone}</strong></p>
                <p class='fade-in'>{insights}</p>
            </div>
        """, unsafe_allow_html=True)

        # Section-Specific Feedback
        sections = [
            ("Profile Optimization", positioning_score, 40, st.session_state.profile_questions, st.session_state.responses[:10]),
            ("Network Growth", presence_score, 35, st.session_state.network_questions, st.session_state.responses[10:20]),
            ("Content Strategy", content_score, 35, st.session_state.content_questions, st.session_state.responses[20:30]),
            ("Personal Value Growth", profit_score, 25, 
             st.session_state.founder_questions if st.session_state.role == "Founder" else st.session_state.creator_questions, 
             st.session_state.responses[30:35])
        ]

        for section_name, score, max_score, questions, responses in sections:
            feedback = get_section_feedback(section_name, score, max_score, st.session_state.role)
            st.markdown(f"""
                <div class='result-section'>
                    <h3 class='fade-in'>📌 {section_name} (Score: {score:.0f}/{max_score})</h3>
                    <p class='fade-in'><strong>Insight:</strong> {feedback['insight']}</p>
                    <p class='fade-in'><strong>Action:</strong> {feedback['action']}</p>
                </div>
            """, unsafe_allow_html=True)

            # Display individual question responses
            ideal_answers = {
                "Profile Optimization": [
                    "Yes, a roadmap ensures sustainable brand and audience growth.",
                    "Yes, and I use it consistently across my content and bio.",
                    "Yes, and my niche is clearly defined in my content.",
                    "Yes, a fully optimized profile increases follower trust and inbound opportunities.",
                    "Yes, and I tailor my content to their interests and needs.",
                    "Yes, and my content directly addresses their problems, making me a must-follow.",
                    "Yes, and I highlight this in my content and profile messaging.",
                    "Yes, a compelling reason drives audience engagement and opportunities.",
                    "No, because my positioning ensures I’m recognized in my niche.",
                    "Yes, and I showcase them on my LinkedIn profile and content."
                ],
                "Network Growth": [
                    "Yes, and I actively engage to build relationships.",
                    "Yes, regular engagement strengthens audience retention and trust.",
                    "Yes, my content attracts the right audience consistently.",
                    "Yes, Groups and Events enhance engagement and community-building.",
                    "Yes, my LinkedIn brand brings consistent inbound opportunities.",
                    "Yes, speaking and collaboration invites show that my brand is working.",
                    "Yes, my DMs contain quality connections and opportunities.",
                    "Yes, being featured increases my visibility and credibility.",
                    "Yes, connecting with influencers expands my reach and opportunities.",
                    "Yes, I’ve converted connections into meaningful professional outcomes."
                ],
                "Content Strategy": [
                    "Yes, consistency drives audience growth and engagement.",
                    "Yes, and my content strategy supports my long-term positioning.",
                    "Yes, diversifying content formats increases audience engagement.",
                    "Yes, strong engagement signals audience loyalty and brand influence.",
                    "Yes, a clear strategy aligns my content with my brand goals.",
                    "Yes, being featured amplifies my reach and credibility.",
                    "Yes, storytelling makes my content more relatable and engaging.",
                    "Yes, tracking analytics helps me optimize my content strategy.",
                    "Yes, my content has led to media and podcast opportunities.",
                    "Yes, a clear CTA drives audience action and engagement."
                ],
                "Personal Value Growth": [
                    "Yes, my positioning attracts high-value opportunities.",
                    "Yes, LinkedIn is a recruiting tool for top talent.",
                    "Yes, my content is designed to drive business opportunities.",
                    "Yes, I’m seen as a leader in my category.",
                    "Yes, my LinkedIn presence gets me featured in industry discussions."
                ] if st.session_state.role == "Founder" else [
                    "Yes, my positioning attracts brands for partnerships.",
                    "Yes, a loyal community increases engagement potential.",
                    "Yes, my content creates direct revenue opportunities.",
                    "Yes, my brand commands premium rates.",
                    "Yes, I’m recognized as an expert in my niche."
                ]
            }[section_name]

            for i, (q, r, ideal) in enumerate(zip(questions, responses, ideal_answers)):
                status = "✅" if r == "Yes" else "🟡"
                st.markdown(f"""
                    <div class='result-section'>
                        <p class='fade-in'>
                            Q{i+1}: {q}<br>
                            Your Answer: <span class='highlighted-answer'>{status} {r}</span><br>
                            Ideal Answer: {ideal}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        # Next Steps and CTA
        st.markdown(f"""
            <div class='result-section'>
                <h3 class='fade-in'>Next Steps:</h3>
                <ul class='fade-in'>{"".join(f"<li>{step}</li>" for step in next_steps)}</ul>
                <p class='fade-in'><strong>🔹 {cta}</strong></p>
            </div>
        """, unsafe_allow_html=True)

        # Redirect button
        if st.button("Hit Me to Grow Your LinkedIn"):
            st.markdown(f'<meta http-equiv="refresh" content="0; url=https://colossal-trader-404.kit.com/666178cb57">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()