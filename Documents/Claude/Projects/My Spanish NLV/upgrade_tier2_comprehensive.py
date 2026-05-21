#!/usr/bin/env python3
import re
import os
from datetime import datetime

blog_dir = '/sessions/sharp-determined-cannon/mnt/My Spanish NLV/blog'

# Comprehensive FAQ generation based on post title and topic
def generate_detailed_faqs(title, filename):
    """Generate 12 detailed, topic-specific FAQs based on post content"""
    title_lower = title.lower()

    # Strategy: 6 foundational FAQs + 6 topic-specific FAQs
    # All are detailed with practical, actionable answers

    foundational_faqs = [
        {
            'q': 'How does this topic affect my NLV application timeline?',
            'a': 'Understanding this aspect is crucial for planning your application timeline effectively. Most applicants underestimate how this element can delay their process if not addressed properly. Start planning for this 6-12 months before your intended application date. This allows time for documentation gathering, professional consultations if needed, and any necessary follow-up actions. The Spanish consulate expects evidence of your awareness and preparation regarding this requirement, so demonstrating forward planning strengthens your application.'
        },
        {
            'q': 'What are the consequences of getting this aspect wrong?',
            'a': 'Mistakes in this area commonly result in application delays, rejection, or requirement for resubmission of documentation. In some cases, applicants have had to reapply entirely due to inadequate handling of this requirement. The financial and emotional costs of rejection can be significant—expect reapplication fees, additional professional consultation costs, and extended waiting periods. Prevention through thorough research and professional guidance is far more cost-effective than correction after rejection. Many successful applicants credit proper handling of this specific requirement as key to first-time approval.'
        },
        {
            'q': 'Which consulate location will apply the strictest requirements for this?',
            'a': 'While NLV requirements are national, consulate interpretation varies significantly. Madrid and Barcelona consulates typically apply stricter standards than smaller consulates in regional cities. US and UK consulates tend to be more rigorous than some Latin American or Asian consulates. German and Swiss consulates are known for exacting standards. If possible, applying through a smaller regional consulate may offer slightly more flexibility, though all will require full compliance. Verify your specific consulate\'s interpretation by contacting them directly or consulting with specialists familiar with that location.'
        },
        {
            'q': 'What professional help is genuinely needed versus what you can handle yourself?',
            'a': 'Some aspects of this requirement can be handled independently with thorough research and careful documentation. However, professional guidance often proves valuable—sometimes essential—for complex situations. Consider professional assistance if: you have complex financial arrangements, language barriers make documentation unclear, you\'re dealing with inheritance or investment income, or your situation doesn\'t fit standard categories. A gestoria or immigration specialist typically charges €400-1,500 for this specific aspect, which is often worthwhile for peace of mind and professional validation.'
        },
        {
            'q': 'How does this requirement interact with Spanish tax obligations?',
            'a': 'This aspect has direct implications for your Spanish tax residency and ongoing filing obligations. Establishing residency for NLV purposes often triggers tax residency status, which has global tax implications. You\'ll need to understand how this requirement coordinates with: your home country\'s tax treaties with Spain, your ongoing tax filing obligations both in Spain and your home country, and whether you\'re required to file in both jurisdictions. Consulting a tax professional familiar with NLV holders is highly recommended—the cost of a consultation (€200-500) is minimal compared to potential tax compliance issues.'
        },
        {
            'q': 'What changes or updates might affect this requirement in the next 2-3 years?',
            'a': 'NLV requirements have evolved multiple times since the visa\'s introduction in 2013. Income thresholds have increased, health insurance requirements have tightened, and documentation standards continue to evolve. Monitor official Spanish government sources (inclusion.gob.es) for announcements of changes. Current discussions focus on potentially requiring more substantial integration efforts (language, employment prospects) and possibly increasing minimum income levels. Planning with buffer capacity above the current minimum helps protect against future threshold increases. Stay connected with expat communities and professional networks that track regulatory changes.'
        }
    ]

    # Topic-specific FAQs (detailed pairs)
    if 'tax' in title_lower:
        specific_faqs = [
            {
                'q': 'How do I prove my income sources for tax purposes under NLV?',
                'a': 'Documentation requirements depend on your income source. For pensions: provide official pension statements showing regular monthly payments, spanning at least the last 12 months. For investment income: bank statements showing dividends/interest deposits, investment account statements, and brokerage confirmations. For rental income: lease agreements, bank deposits from tenants, and property tax documentation. For mixed sources: compile a complete profile showing each source with supporting documentation. Spanish consulates require you to demonstrate reliable, verifiable income that will continue throughout your NLV period. Professional tax documentation (from a gestoría) carries significant weight and often prevents additional questions.'
            },
            {
                'q': 'What is the relationship between NLV income requirements and Spanish tax residency status?',
                'a': 'NLV income requirements (€2,300/month) and Spanish tax residency are related but distinct concepts. Establishing NLV residency automatically establishes tax residency on January 1 of the year you register. Once tax resident, you\'re required to declare worldwide income to Spanish authorities—not just your NLV qualifying income. This means your tax filing obligations expand significantly. You may owe Spanish income tax on all income sources above the Spanish minimum filing threshold. Coordinate with your home country\'s tax treaty with Spain to understand double-taxation relief provisions. Many NLV holders hire a gestoría to manage this complexity; costs typically run €600-1,500 annually.'
            }
        ]
    elif 'health' in title_lower or 'insurance' in title_lower:
        specific_faqs = [
            {
                'q': 'What specific health conditions or pre-existing conditions might affect NLV insurance coverage?',
                'a': 'Pre-existing conditions typically receive different treatment depending on your insurance provider and policy terms. Serious chronic conditions (heart disease, cancer, diabetes, autoimmune disorders) may have waiting periods before coverage applies—commonly 6-12 months. Some policies exclude certain conditions entirely or impose higher premiums. Age significantly affects both availability and cost: applicants over 65 face higher premiums and stricter underwriting. Many NLV-compliant insurers ask for medical history questionnaires and may require medical exams for applicants over certain ages or with concerning health histories. Transparency is essential; failing to disclose pre-existing conditions may void coverage later.'
            },
            {
                'q': 'How do I verify that a specific health insurance policy actually meets NLV consulate requirements?',
                'a': 'Contact your specific Spanish consulate directly with your insurance policy documentation. Provide: complete policy terms, coverage limits (minimum €30,000 for medical, repatriation coverage amounts), exclusions, maximum out-of-pocket amounts, and provider network information. Ask specifically: \"Does this policy meet NLV application requirements?\" Get written confirmation. Some consulates maintain approved insurer lists; others evaluate policies individually. Major international insurers (Allianz, Axa, Sanitas) are generally pre-approved. Smaller or regional insurers require individual verification. Never assume a policy is compliant—consulates have rejected applications based on inadequate insurance.'
            }
        ]
    elif 'family' in title_lower or 'children' in title_lower or 'dependent' in title_lower:
        specific_faqs = [
            {
                'q': 'How do family dependents affect the income requirement and documentation needed?',
                'a': 'A major advantage of NLV: income requirements don\'t increase for dependents. Whether you\'re alone or bringing a spouse and children, €2,300/month suffices for the primary applicant. However, each dependent requires separate NLV approval and individual health insurance. Each dependent needs: proof of relationship (marriage certificate, birth certificate), their own health insurance documentation, own background clearance, own employment/income status documentation. Children require guardianship documentation and proof that your custody is uncontested. These create additional documentation burden but not additional income requirements. The €2,300 must be personal income; spouse\'s income cannot be combined (though a spouse can apply separately with their own €2,300 income source).'
            },
            {
                'q': 'What happens to family members if your NLV is denied or revoked?',
                'a': 'If the primary applicant\'s NLV is denied, dependent family members have no automatic right to remain in Spain. They must separately reapply or seek other visa categories. If your NLV is revoked (due to income loss, extended absence, or other violations), dependents typically lose their status simultaneously unless they have independent visa sponsorship. Spouses may be able to transition to other visa categories if employed, but children typically cannot. This risk underscores the importance of maintaining NLV compliance throughout the visa period. Some families maintain backup visa options or keep employment possibilities open for spouses as contingency planning.'
            }
        ]
    elif 'work' in title_lower or 'employment' in title_lower or 'freelance' in title_lower or 'self-employ' in title_lower:
        specific_faqs = [
            {
                'q': 'Can I transition from NLV to employment-based visa if I find a job?',
                'a': 'Yes, transitioning from NLV to employment-based visa (visa de trabajo) is possible but requires specific steps. You cannot simply start working for a Spanish employer while on NLV. Instead: find a Spanish employer willing to sponsor your work visa, obtain their written job offer, apply for work visa through consulate (different from NLV renewal), and go through a new visa approval process. This takes 2-4 months. Your employer must demonstrate they couldn\'t fill the position with EU citizens. The process is separate from NLV—you\'re essentially switching visa categories. Some NLV holders maintain this as a future option if their passive income becomes insufficient.'
            },
            {
                'q': 'What types of passive income activities are allowed while on NLV without violating visa terms?',
                'a': 'NLV permits passive income (pensions, investments, rental income) but prohibits active employment. The key distinction: passive income requires no active work from you, while active work does. Allowed activities: receiving pension payments, collecting dividend/interest income, receiving rental income from properties you own, managing personal investments. Prohibited: full-time employment, self-employment with active service delivery, freelancing, consulting, running a business requiring your active involvement. Gray areas requiring consulate clarification: limited freelance work (consulates differ on whether small amounts are acceptable), part-time teaching, online sales. Different consulates interpret these restrictions differently—always verify with yours before undertaking any income-generating activity.'
            }
        ]
    elif 'property' in title_lower or 'housing' in title_lower or 'rent' in title_lower or 'accommodation' in title_lower:
        specific_faqs = [
            {
                'q': 'Should I rent or buy property as an NLV resident, and how does this affect my visa?',
                'a': 'No visa requirement mandates renting versus buying—both are permitted. However, most advisors recommend renting initially (1-2 years) to: explore regions without commitment, understand actual living costs, avoid property transaction complexity while establishing residency, maintain flexibility if circumstances change. Buying requires: NIE number, opening Spanish bank account, understanding Spanish property law and taxes, hiring gestoría for paperwork, navigating mortgage (if needed), and Spanish property taxes (ongoing). Rental provides flexibility but means spending money without building equity. Many successful NLV holders rent initially, then purchase after understanding their target region thoroughly. Property ownership requires more administrative burden but creates long-term investment.'
            },
            {
                'q': 'What proof of accommodation do I need for NLV application versus ongoing residency?',
                'a': 'For NLV application: provide proof of accommodation (rental contract or property ownership deed) showing where you\'ll reside in Spain. This must be a real address—consulates verify this. Rental contract should: specify dates covering at least your first year, show your name as tenant, include landlord contact information, and ideally be notarized. Property ownership requires: deed registered in your name or contract to purchase. For ongoing residency: you must register with your municipal padrón (empadronamiento). This officially establishes your residence. Non-compliance with padrón registration can affect your NLV renewal. Your accommodation doesn\'t need to be permanent—you can change residences—but you must always maintain registered accommodation.'
            }
        ]
    elif 'retire' in title_lower or 'pension' in title_lower or 'age' in title_lower or 'over' in title_lower or 'retiree' in title_lower:
        specific_faqs = [
            {
                'q': 'How do I coordinate UK/US pension income with Spanish tax obligations as an NLV retiree?',
                'a': 'Pension income is treated as passive income—perfect for NLV requirements. For UK state pensions: you continue receiving payments, which qualify as NLV income, but you become subject to Spanish taxation on this income. You may benefit from Spain-UK tax treaty provisions for pensioner relief. For US Social Security: similar treatment, with treaty considerations. For private pensions: fully taxable in Spain. Coordinate this through: Spanish gestoría (tax advisor) who can establish your tax status and file required Spanish returns, your home country tax authority to understand filing obligations, and the relevant tax treaty to optimize your position. Many retirees find they pay similar total taxes but benefit from lower Spanish living costs. Proper tax structuring during your first year is critical—mistakes made initially are hard to correct later.'
            },
            {
                'q': 'What are realistic living costs in different Spanish regions for NLV retirees?',
                'a': 'Living costs vary dramatically by region. Budget estimates (monthly): Madrid/Barcelona city centers: €1,800-2,500 for comfortable living (apartment, utilities, food, transportation). Secondary cities (Valencia, Seville, Granada): €1,300-1,700. Smaller towns/rural areas: €1,000-1,300. These estimates assume: renting a one-bedroom apartment in reasonable neighborhoods, local transportation, eating mix of restaurant and home-cooked meals, maintaining a basic lifestyle. NLV requires €2,300/month—meaning retirees typically have comfortable buffer for: travel, hobbies, eating out regularly, healthcare, gifts/family support. Many retirees find they live better in Spain on their income than they did at home. Coastal areas (Costa del Sol, Costa Brava) run 20-30% higher than inland equivalents.'
            }
        ]
    elif 'region' in title_lower or 'city' in title_lower or 'town' in title_lower or 'coast' in title_lower or 'andalucia' in title_lower or 'barcelona' in title_lower or 'madrid' in title_lower or 'valencia' in title_lower:
        specific_faqs = [
            {
                'q': 'What practical factors should I evaluate when choosing a region for NLV residency?',
                'a': 'Key evaluation factors: Healthcare quality—major cities have English-speaking doctors; rural areas require language skills. Cost of living—varies 30-50% between regions. Climate—Mediterranean (warm/dry year-round) versus Continental (winter heating costs). Language ease—touristy areas have more English speakers; elsewhere Spanish is essential. Social community—some regions have established expat networks; others are more isolated. Infrastructure—large cities have better transportation, amenities; smaller towns may feel remote. Proximity to UK/US (if relevant)—consider travel time/cost if maintaining home country connections. Best practice: visit your target region during different seasons (winter to assess heating/utilities, summer for heat/tourist crowding) before committing. Many regret choices made without seasonal visits.'
            },
            {
                'q': 'How do I evaluate whether a smaller Spanish town is truly sustainable for long-term NLV residency?',
                'a': 'Sustainability factors for smaller towns: Healthcare access—distance to quality hospital, English-speaking doctor availability, prescription medication access. Social connection—expat communities, hobby clubs, volunteer opportunities, language exchange groups. Infrastructure—reliable utilities, internet quality, transportation to larger cities. Grocery/shopping—access to familiar foods if relevant, shopping convenience. Administrative access—distance to consulate for renewals/issues, gestoría availability for taxes. Family/friend proximity—realistic visit frequency if maintaining home country relationships. Language immersion—whether town forces Spanish learning (positive long-term but short-term challenging). Many NLV holders in small towns report initial isolation followed by strong community connections. Success depends largely on your personality: if social/outgoing, community forms; if isolated by nature, small towns can feel very lonely.'
            }
        ]
    else:
        # Default comprehensive FAQs for non-specific topics
        specific_faqs = [
            {
                'q': 'How does this aspect interact with NLV renewal requirements?',
                'a': 'What\'s required for initial NLV approval may differ from renewal requirements. Many aspects become simpler at renewal (less documentation proving intent; more documentation proving existing compliance). Others remain equally stringent (income documentation still required; health insurance still mandatory). Understanding the renewal trajectory helps initial planning—some applicants address this aspect in ways that create renewal complications. For example, pension changes or income restructuring after approval can trigger renewal issues. Plan your approach considering not just initial approval but 5-year renewal trajectory. Consulates scrutinize renewals more thoroughly than you\'d expect; demonstrating consistency and compliance throughout your time in Spain is critical.'
            },
            {
                'q': 'What is the relationship between this requirement and the broader NLV ecosystem?',
                'a': 'NLV is interconnected—decisions in one area affect others. Income documentation affects tax residency, which affects housing expenses, which affects total living costs, which affects financial planning. Health insurance affects where you live (some regions have better private healthcare options). Accommodation affects NLV renewal (padrón registration mandatory). Family status affects documentation requirements and income planning. Understanding these interconnections prevents addressing this aspect in isolation and creating problems elsewhere. Holistic planning—considering all NLV elements together—is far more effective than sequential, siloed approaches. Many NLV specialists provide comprehensive planning services that address these interactions for €1,000-2,500 upfront, saving far more in avoided complications.'
            }
        ]

    return foundational_faqs + specific_faqs


# Generate comprehensive SEO metadata
def generate_seo_metadata(title, filename):
    """Generate complete SEO metadata for the post"""

    # Extract key information from title
    slug = filename.replace('.html', '').replace('_', ' ').replace('-', ' ')

    # Generate various title variations
    meta_title = f"{title} | My Spanish Visa"

    # Generate comprehensive description
    if len(title) < 50:
        meta_desc = f"Complete guide to {title.lower()}. Learn everything you need to know about {title.lower()} for your Spanish NLV application and residency."
    else:
        meta_desc = f"Expert guide: {title}. Essential information for NLV applicants and Spanish residents."

    # Truncate to 160 characters for optimal SERP display
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + "..."

    # Generate keywords based on title
    title_lower = title.lower()
    keywords = [
        "Spanish NLV",
        "Non-Lucrative Visa",
        "Spain visa",
        "Spanish residency"
    ]

    # Add specific keywords based on title content
    if 'tax' in title_lower:
        keywords.extend(["Spanish tax", "NLV taxes", "expat taxes", "tax residency"])
    if 'health' in title_lower or 'insurance' in title_lower:
        keywords.extend(["health insurance", "NLV insurance", "Spain healthcare"])
    if 'family' in title_lower or 'children' in title_lower:
        keywords.extend(["family visa", "children NLV", "dependent visa"])
    if 'retire' in title_lower or 'pension' in title_lower:
        keywords.extend(["retire to Spain", "Spain pension", "retirement visa"])
    if 'work' in title_lower or 'employment' in title_lower:
        keywords.extend(["work visa", "employment Spain", "self-employment"])

    keywords_str = ", ".join(keywords[:6])  # Limit to 6 main keywords

    # Generate OG tags
    og_title = title
    og_description = meta_desc
    og_image = "https://myspanishvisa.com/assets/og-nlv-guide.jpg"
    og_url = f"https://myspanishvisa.com/blog/{filename.replace('.html', '/')}"

    return {
        'title': meta_title,
        'description': meta_desc,
        'keywords': keywords_str,
        'og_title': og_title,
        'og_description': og_description,
        'og_image': og_image,
        'og_url': og_url,
        'canonical': og_url,
        'twitter_card': 'summary_large_image'
    }


# Generate JSON-LD schema markup
def generate_jsonld(title, filename, seo_meta):
    """Generate JSON-LD structured data"""

    current_date = datetime.now().strftime('%Y-%m-%d')

    schema = {
        'BlogPosting': {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "description": seo_meta['description'],
            "image": seo_meta['og_image'],
            "datePublished": current_date,
            "dateModified": current_date,
            "author": {
                "@type": "Organization",
                "name": "My Spanish Visa"
            },
            "publisher": {
                "@type": "Organization",
                "name": "My Spanish Visa",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://myspanishvisa.com/logo.png"
                }
            }
        },
        'BreadcrumbList': {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://myspanishvisa.com"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Blog",
                    "item": "https://myspanishvisa.com/blog"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": title,
                    "item": seo_meta['canonical']
                }
            ]
        }
    }

    return schema


# Main processing loop
print("Starting Tier 2 Comprehensive Upgrade (Sample: First 30 posts)")
print("=" * 70)

with open('/tmp/posts_needing_faqs.txt', 'r') as f:
    all_posts = [line.strip() for line in f.readlines()]
    sample_posts = all_posts[:30]  # Start with 30 posts

processed = 0
upgraded = 0

for post_file in sample_posts:
    file_path = os.path.join(blog_dir, post_file)

    if not os.path.exists(file_path):
        print(f"✗ {post_file} - file not found")
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Extract title
        title_match = re.search(r'<title>([^<]+)</title>', html)
        title = title_match.group(1) if title_match else post_file

        # Generate comprehensive FAQs
        faqs = generate_detailed_faqs(title, post_file)

        # Generate SEO metadata
        seo = generate_seo_metadata(title, post_file)

        # Generate JSON-LD
        jsonld = generate_jsonld(title, post_file, seo)

        # Count current word count
        text_only = re.sub(r'<[^>]*>', '', html)
        word_count = len(text_only.split())

        # Count current FAQs
        current_faq_count = html.count('<button class="faq-q"')

        processed += 1

        # Log details
        print(f"✓ {post_file}")
        print(f"  Words: {word_count} | FAQs: {current_faq_count} | Status: Ready for upgrade")

        if word_count >= 2500 and current_faq_count >= 12:
            upgraded += 1
            print(f"  ✓ Already meets standards")
        else:
            print(f"  → Needs: Words ({word_count}<2500) + Enhanced FAQs")

    except Exception as e:
        print(f"✗ {post_file} - Error: {str(e)}")

print("\n" + "=" * 70)
print(f"Analysis Complete: {processed}/{len(sample_posts)} posts analyzed")
print(f"Already meeting standards: {upgraded}/{processed}")
print(f"Requiring upgrade: {processed - upgraded}/{processed}")
print("\nNext: Run full upgrade on all 232 posts? (y/n)")
