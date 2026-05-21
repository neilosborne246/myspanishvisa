#!/usr/bin/env python3
import re
import os

blog_dir = '/sessions/sharp-determined-cannon/mnt/My Spanish NLV/blog'

# Topic-aware FAQ templates - customize based on post title keywords
def generate_additional_faqs(title):
    """Generate 6 contextually relevant FAQs based on post title"""
    title_lower = title.lower()

    # Base FAQs that apply to most NLV topics
    base_faqs = [
        {
            'q': 'How does this relate to my overall NLV application requirements?',
            'a': 'This aspect is interconnected with your broader NLV visa application. Understanding the full context of NLV requirements—including income, health insurance, documentation, and residency rules—ensures comprehensive preparation. Consider how this specific topic integrates with your financial planning, healthcare needs, and administrative obligations when relocating to Spain.'
        },
        {
            'q': 'What are the most common mistakes people make regarding this aspect?',
            'a': 'Common errors include incomplete documentation, misunderstanding timelines, overlooking regional variations, and failing to plan ahead. Most mistakes are preventable through thorough research, professional consultation when needed, and careful attention to official requirements. Learning from others\' experiences helps you avoid costly delays or rejections.'
        },
        {
            'q': 'Are there regional differences I should account for?',
            'a': 'Yes, Spain\'s autonomous communities have varying implementation approaches. While national NLV requirements are consistent, administration, costs, and local services differ. Barcelona and Madrid operate differently than Granada or smaller towns. Research your specific intended region to understand how this topic applies locally. Expat groups in your target region provide invaluable local insights.'
        },
        {
            'q': 'How should I plan financially for this?',
            'a': 'Develop a comprehensive financial plan that incorporates this aspect into your overall budget. Identify direct costs, contingency amounts for unexpected expenses, and timing of cash flow. Consider both first-year setup costs and ongoing annual expenses. Conservative budgeting prevents financial stress during relocation and helps you establish stability sooner.'
        },
        {
            'q': 'Where can I find official guidance on this requirement?',
            'a': 'Official sources include your country\'s Spanish consulate website, the Spanish government\'s immigration portal (inclusion.gob.es), and official municipal websites for the region where you plan to reside. Your consulate\'s visa section provides authoritative guidance. Be cautious with unofficial sources; always verify critical information against official government sources before acting on it.'
        },
        {
            'q': 'When should I address this as part of my NLV timeline?',
            'a': 'Timing varies by topic, but advance planning (6-12 months before applying) reduces stress and prevents delays. Some aspects require immediate attention upon arriving in Spain, while others can be handled gradually. Understanding the proper sequence and timeline for different NLV-related tasks ensures efficient relocation and residency establishment.'
        }
    ]

    # Topic-specific FAQs based on keywords
    if 'tax' in title_lower:
        topic_faqs = [
            {
                'q': 'How do Spanish tax rules affect my NLV residency status?',
                'a': 'Tax residency and NLV residency are related but distinct. Establishing tax residency in Spain affects your tax obligations globally. Understanding both systems prevents double taxation issues and optimizes your financial position. Many NLV holders benefit from consulting tax professionals in both countries to structure income efficiently while complying with Spanish tax law.'
            },
            {
                'q': 'What documentation do I need for tax compliance as an NLV resident?',
                'a': 'You\'ll need: NIE (foreigner ID number), registration with Spanish tax authorities (Hacienda), bank statements, investment documentation, and income source verification. Keeping organized records of all income, deductions, and transactions simplifies tax filing. Spanish tax forms can be complex; many NLV holders use gestoría (tax advisory) services for compliance and optimization.'
            }
        ]
    elif 'health' in title_lower or 'insurance' in title_lower:
        topic_faqs = [
            {
                'q': 'How do I choose the right health insurance provider for my NLV needs?',
                'a': 'Compare providers offering NLV-compliant policies, checking coverage breadth, premium costs, deductibles, and provider networks. Some specialize in expat insurance. Read reviews from other NLV holders. Verify the policy meets your specific health needs and covers the regions where you\'ll spend time. Transitioning to public healthcare later is an option once residency is established.'
            },
            {
                'q': 'What happens to my health insurance if circumstances change during my NLV?',
                'a': 'Insurance can typically be modified if you move regions, age significantly, or experience health changes. Some policies have provisions for switching to public healthcare. If you become employed, employment-based insurance may replace NLV insurance. Maintain continuous coverage to avoid gaps; contact your provider immediately if changes occur.'
            }
        ]
    elif 'family' in title_lower or 'children' in title_lower or 'spouse' in title_lower:
        topic_faqs = [
            {
                'q': 'How do family members affect my NLV requirements and costs?',
                'a': 'NLV income requirements remain €2,300/month regardless of dependents—a major advantage. However, each dependent requires their own documentation and permit. Healthcare insurance costs scale with family size. Housing and living costs increase with family members. Overall, family relocation on NLV is financially feasible; the stable income requirement actually creates predictability.'
            },
            {
                'q': 'What are the custody and guardianship implications for children on NLV?',
                'a': 'Legal custody must be established and documented. Single parents need formal custody documents. Shared custody requires consent from both parents. Guardianship documentation must be current and notarized. Court-stamped orders are required. International custody complications require legal consultation. Addressing this thoroughly prevents visa approval delays or complications.'
            }
        ]
    elif 'work' in title_lower or 'employment' in title_lower or 'self-employ' in title_lower:
        topic_faqs = [
            {
                'q': 'Can I transition from NLV to employment-based residence?',
                'a': 'Yes, you can change visa categories if you secure employment. This requires finding a Spanish employer willing to sponsor you and obtaining a work visa. The process differs from NLV application. Some NLV holders work part-time legally; consult your consulate about employment restrictions. Transitioning visas requires planning and legal guidance.'
            },
            {
                'q': 'How does working while on NLV affect my income verification?',
                'a': 'NLV specifically requires pasiva (passive income), not active employment. Working full-time typically disqualifies you from NLV. Part-time work may be permitted in some circumstances; verify with your consulate. Active employment income shouldn\'t substitute for required passive income. If circumstances change, discuss options with immigration authorities before making employment commitments.'
            }
        ]
    elif 'property' in title_lower or 'housing' in title_lower or 'rent' in title_lower:
        topic_faqs = [
            {
                'q': 'Should I rent or buy property as an NLV resident?',
                'a': 'Most new NLV arrivals rent initially to explore regions, understand costs, and avoid commitment before establishing residency. Buying property is possible but involves legal complexity, mortgage considerations, and tax implications. Renting provides flexibility; purchasing builds equity. Many NLV holders rent 1-3 years before purchasing. Consider your long-term plans when deciding.'
            },
            {
                'q': 'What legal protections do I have as a rental tenant in Spain?',
                'a': 'Spain has tenant protection laws covering lease terms, eviction procedures, and maintenance responsibilities. Written contracts are essential. Landlords must provide property in habitable condition; tenants must maintain the property. Disputes are resolved through legal channels. Having a written lease protects both parties. Many expat organizations provide lease templates and advice.'
            }
        ]
    elif 'retire' in title_lower or 'pension' in title_lower or 'age' in title_lower or 'over' in title_lower:
        topic_faqs = [
            {
                'q': 'How does retirement in Spain differ from retirement in my home country?',
                'a': 'Spanish retirement offers lower costs, excellent healthcare, favorable climate, and vibrant social culture. However, you\'re far from family, face language barriers, and navigate unfamiliar healthcare/administrative systems. Many retirees maintain dual residences or spend part of the year in home countries. Retirement should be intentional, not just cost-driven; lifestyle alignment matters most.'
            },
            {
                'q': 'What pension sources qualify for NLV income requirements?',
                'a': 'Government pensions (state pensions, military pensions), private pensions, retirement annuities, and investment-generated income all qualify. Each source requires documentation (pension statements, investment account statements, tax records). Combined sources are acceptable if each individually documents their income. Pension income must be reliable and verifiable.'
            }
        ]
    elif 'region' in title_lower or 'city' in title_lower or 'town' in title_lower or 'area' in title_lower or 'coast' in title_lower:
        topic_faqs = [
            {
                'q': 'How do I evaluate whether this region is right for me?',
                'a': 'Visit during different seasons, explore neighborhoods at various times of day, research climate and weather patterns, investigate healthcare facilities and services, assess expat community presence, evaluate cost of living, and speak with current residents. Join regional Facebook groups to ask questions directly. Extended visits (1-2 weeks minimum) provide better insight than brief tours. Many successful relocations start with thorough regional evaluation.'
            },
            {
                'q': 'What are the practical differences between living in this region versus major cities?',
                'a': 'Major cities offer more services, international options, and cultural diversity but cost more and feel less intimate. Secondary cities balance affordability with amenities. Smaller towns provide community feel and lower costs but fewer services. Your priorities—cultural access, healthcare specialization, climate, cost, or community—should guide regional choice. No region is universally "best"; fit depends on personal preferences.'
            }
        ]
    else:
        # Default general FAQs for non-specific topics
        topic_faqs = [
            {
                'q': 'How is this aspect handled differently by different consulates?',
                'a': 'While NLV requirements are national, consulate interpretation and implementation vary slightly. Some consulates are more flexible; others enforce stricter standards. Your specific consulate\'s website and direct communication clarify their requirements. When requirements seem ambiguous, contact your consulate directly rather than assuming based on others\' experiences.'
            },
            {
                'q': 'What is the relationship between this topic and my overall residency timeline?',
                'a': 'Understanding how individual components fit into the complete residency journey prevents bottlenecks and delays. Some aspects require attention before others. Strategic sequencing ensures efficient progress. Consider the full timeline from pre-application through first-year residency establishment when planning this particular element.'
            }
        ]

    # Return 6 total FAQs: some from base + some from topic-specific
    if len(topic_faqs) >= 2:
        return base_faqs[:4] + topic_faqs[:2]
    else:
        return base_faqs[:6]


# Process first 50 posts from the list
with open('/tmp/posts_needing_faqs.txt', 'r') as f:
    posts_to_process = [line.strip() for line in f.readlines()][:50]

print(f"Processing {len(posts_to_process)} posts in Batch 1...")
success_count = 0

for post_file in posts_to_process:
    file_path = os.path.join(blog_dir, post_file)

    if not os.path.exists(file_path):
        print(f"✗ {post_file} - file not found")
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Extract title for FAQ generation
        title_match = re.search(r'<title>([^<]+)</title>', html)
        title = title_match.group(1) if title_match else post_file

        # Generate 6 additional FAQs based on topic
        additional_faqs = generate_additional_faqs(title)

        # Build new FAQ HTML
        new_faqs_html = ''
        for faq in additional_faqs:
            new_faqs_html += f'''                    <div class="faq-item">
                        <button class="faq-q" aria-expanded="false">
                            <span>{faq['q']}</span>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                            </svg>
                        </button>
                        <div class="faq-a">{faq['a']}</div>
                    </div>
'''

        # Insert new FAQs before closing faq-section tag
        pattern = r'(<div class="faq-item">.*?</div>)\s*(</div>\s*</div>\s*</section>)'
        replacement = r'\1' + '\n' + new_faqs_html.rstrip() + r'\n                </div>\2'

        html_updated = re.sub(pattern, replacement, html, flags=re.DOTALL, count=1)

        if html_updated == html:
            print(f"✗ {post_file} - could not insert FAQs")
            continue

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_updated)

        # Verify count
        faq_count = html_updated.count('<button class="faq-q"')
        success_count += 1
        print(f"✓ {post_file}: {faq_count} total FAQs")

    except Exception as e:
        print(f"✗ {post_file} - error: {str(e)}")

print(f"\n✓ Batch 1 Complete: {success_count}/{len(posts_to_process)} posts successfully expanded to 12 FAQs")
print(f"\nRemaining posts for Batches 2-5: {232 - len(posts_to_process)}")
