# Email Nurture Sequences — My Spanish Visa
**Brand:** myspanishvisa.com | Modern, Premium, Expat-Focused  
**Audience:** UK, US, Canada, Australia, Ireland, South Africa English speakers  
**Last Updated:** April 2026

---

## QUICK REFERENCE

| Sequence | Trigger | Duration | Goal | Email Count |
|----------|---------|----------|------|-------------|
| **Sequence 1** | Eligibility Check Completed | 14 days | Move qualified leads to consultation booking | 7 |
| **Sequence 2** | Lead Magnet Downloaded (Checklist) | 21 days | Educate + build trust + convert to consultation | 6 |
| **Sequence 3** | Consultation Call Completed | 30 days | Close to paid engagement / retain / collect testimonial | 5 |

---

# SEQUENCE 1: POST-ELIGIBILITY CHECK
## Goal: Move Qualified Leads to Consultation Booking

### Sequence Overview

| Email | Day | Subject | Status | Branch |
|-------|-----|---------|--------|--------|
| 1 | 0 | Results Ready + Personalized Next Steps | Immediate | All branches |
| 2 | 2 | Your NLV Path Explained (Simple Version) | Follow-up | A: Likely Eligible |
| 2 | 2 | Your Options Are Better Than You Think | Follow-up | B: Borderline |
| 2 | 2 | Timing Is Everything for DNV | Follow-up | C: Not Eligible Now |
| 3 | 5 | Real Timeline: What Happens First | Educational | A, B |
| 4 | 7 | 3 Documents You'll Need (No Surprises) | Value | A, B |
| 5 | 10 | Why People Hire Us (Spoiler: It's Not What You Think) | Trust-Build | A, B |
| 6 | 12 | Book Your Consultation — 30 Min, Free | CTA | A, B, C |

### Branching Logic

**Branch A: Likely Eligible**  
User scored high on eligibility assessment. Path: fast-track to consultation booking, build confidence, simplify process.

**Branch B: Borderline**  
User has potential but needs clarity on specific requirements. Path: educational content, address concerns, show flexibility, soft CTA to consultation.

**Branch C: Not Eligible Now**  
User doesn't currently qualify but could in future (e.g., needs work contract, more savings, different visa). Path: nurture for future opportunity, keep engaged, long-term follow-up.

### Send Time Recommendation
- **Email 1 (Day 0):** Immediate, any time within 1 hour of form submission
- **Emails 2–6:** 9 AM in user's local timezone (inferred from IP or ask during form)

### ESP Tags Required
- `seq1_eligibility_check`
- `seg_eligible_a` / `seg_eligible_b` / `seg_eligible_c`
- `ready_for_consultation`
- `nurture_only`

### KPI Benchmarks
- **Open Rate:** 45–55%
- **Click Rate:** 12–18%
- **Reply Rate:** 3–5%
- **Consultation Booking Rate:** 18–25% (Branch A), 8–12% (Branch B), <2% (Branch C)
- **Unsubscribe Rate:** <0.5%

---

## Email 1 — Day 0
**Goal:** Celebrate result, show clear path forward, remove anxiety.

**Subject Line:**  
Your Eligibility Results Are Ready — Here's What's Next  
*A/B Alternative:* Good News on Your Spain Visa Path

**Preview Text:**  
We've reviewed your details. You're closer than you think. Here's what happens now.

**Body Copy:**

Hi [First Name],

Thanks for taking the time to complete your eligibility assessment. We've reviewed what you shared, and we can give you a clear answer.

[Branch A: You're in a strong position for the Non-Lucrative (NLV) Visa. The income requirement is straightforward, your timeline is realistic, and we see a clear path forward.]

[Branch B: You've got options. Your situation is more nuanced than a simple yes/no, but that's exactly why a brief conversation with us is valuable. We can map out which visa actually fits your goals.]

[Branch C: Right now, the visa you're targeting requires something you don't have in place yet—but that doesn't mean the door is closed. We've outlined timing and next steps below.]

The next step isn't complicated. What usually takes 4–6 weeks of research and back-and-forth emails, we can clarify in a 30-minute conversation. No sales pitch. Just honest guidance on your specific situation.

We've got a few slots open this week if you want to book straight away.

**Primary CTA:**  
[Book Your Free Consultation](#)

**Secondary CTA:**  
Reply to this email with your availability.

**Exit Condition:**  
User books a consultation call → moves to post-consultation sequence (Sequence 3).

---

## Email 2 — Day 2 (Branch A: Likely Eligible)
**Goal:** Build confidence, simplify the process, reduce overwhelm.

**Subject Line:**  
Your NLV Visa Path (Simpler Than You'd Think)  
*A/B Alternative:* The NLV Process: Exactly What's Involved

**Preview Text:**  
Three straightforward steps. No surprises. Here's the full timeline.

**Body Copy:**

Hi [First Name],

You asked about the Non-Lucrative Visa for Spain. Let's make this concrete, because most people overthink it.

**The Income Requirement**  
€28,800 per year for a single person (€43,200 for couples). Passive income, pension, investments—they all count. You showed you have this or can hit it. That's the hardest part done.

**The Process (3 Main Steps)**

1. **Document Gathering** (2–3 weeks)  
   Bank statements (12 months), proof of income, ID, police certificate. We help you know exactly what your consulate needs—there's no universal "list," so this is where people waste time.

2. **Application Submission** (2–3 weeks)  
   Your consulate pre-books an appointment. You go in, hand over docs, answer basic questions. It's straightforward.

3. **Waiting** (4–8 weeks after submission)  
   The consulate reviews everything. Most approvals come within this window.

**Total realistic timeline: 3–5 months from start to visa in hand.**

The part people get wrong: they assume each consulate's requirements are identical. They're not. Which is why a lot of DIY applications get sent back incomplete.

That's the gap we fill.

**Primary CTA:**  
Ready to get started? [Book a consultation](#) so we can walk through your specific consulate's quirks and timeline.

**Secondary CTA:**  
Still gathering info? That's fine. Keep this email for reference.

**Exit Condition:**  
User books a consultation → Sequence 3.  
No engagement after Email 6 → assign `nurture_only` tag, move to monthly touchpoint email.

---

## Email 2 — Day 2 (Branch B: Borderline)
**Goal:** Address uncertainty, show options exist, make case for clarification call.

**Subject Line:**  
Your Situation Needs a Real Conversation (Not More Email)  
*A/B Alternative:* Don't Assume You're Ineligible — Here's Why

**Preview Text:**  
One factor is unclear. A 30-minute call could change everything.

**Body Copy:**

Hi [First Name],

Your eligibility assessment came back with a "maybe," and we want to explain why that's not a bad thing.

**What We Saw**

Your income is close to the NLV requirement—or you have income from multiple sources that we need to confirm counts. (Spoiler: it often does, but the rules are specific.)

Alternatively, you might qualify for a different visa that's actually a better fit than the one you were asking about.

**Why This Matters**

Right now, you're assuming you need to hit an exact number. You might not. Or you might already have it without realizing. We've seen both.

A 30-minute call where we walk through your exact situation is the only way to know for sure. No form is detailed enough. Email back-and-forth takes forever. A conversation is the fastest and clearest path.

**What We'd Cover in That Call**

- Which income counts toward the visa requirement (and which doesn't)
- Whether another visa might be a better fit
- A realistic timeline for your situation
- Next steps if you want to move forward

**Primary CTA:**  
[Let's Schedule a Consultation](#) — 30 minutes, free, zero pressure.

**Secondary CTA:**  
Reply with 2–3 times that work best for you.

**Exit Condition:**  
User books a consultation → Sequence 3.  
User unsubscribes → remove from all sequences.

---

## Email 2 — Day 2 (Branch C: Not Eligible Now)
**Goal:** Keep door open, plant seed for future opportunity, position as long-term guide.

**Subject Line:**  
You're Not Ready Yet — But Here's When You Will Be  
*A/B Alternative:* Your Spain Visa Timeline: When to Revisit This

**Preview Text:**  
One thing needs to change. We've outlined when and how.

**Body Copy:**

Hi [First Name],

Your assessment shows you're not quite ready for the visa you were targeting. Let's be direct about why, and what needs to happen.

**What's Missing**

[Your current employment status / savings level / timeline] doesn't quite fit the requirement yet. For the NLV visa, you need €28,800 annual income (verified over 12 months). For DNV, employers need to show they've hired locally first.

**Here's the Good News**

This isn't permanent. Based on what you shared, you're likely 6–18 months away from qualifying, depending on your route.

**What to Do in the Meantime**

If you're on a career path that'll increase your income, get there. If you're saving to hit the threshold, keep going. If you're waiting for a work contract that shows Spanish employment, that's the key blocker—but it's fixable.

We keep people like you in our loop. When you hit that milestone—new job, savings goal reached, work contract in hand—reach out. We'll fast-track your application because we already understand your situation.

**Primary CTA:**  
Bookmark this email. When things change, reply and let us know.

**Secondary CTA:**  
[Read: The Real Timeline for Spain Residency](#) — longer guide that helps you see how you fit in.

**Exit Condition:**  
User replies with an update → move to relevant path (A or B).  
No engagement for 6 months → send re-engagement email, offer to update assessment.

---

## Email 3 — Day 5 (Branches A & B)
**Goal:** Set realistic expectations, build authority through specifics, reduce decision paralysis.

**Subject Line:**  
The Real Timeline: What Happens First  
*A/B Alternative:* Week 1 to Month 5: What You'll Actually Be Doing

**Preview Text:**  
Month by month, what to expect and when to expect it.

**Body Copy:**

Hi [First Name],

Let's walk through the actual timeline so there's no mystery or false expectations.

**Months 1–2: Document Gathering**

This is the unglamorous part, but it's crucial. You'll need:
- 12 months of bank statements (some consulates want 24)
- Proof of income (pension letter, investment statements, employment contract, etc.)
- Police certificate from your home country (takes 2–4 weeks in some places)
- Passport, birth certificate, marriage certificate (if applicable), travel history
- Proof of accommodation in Spain (rental contract, property deed, or letter from friend)

Why does this take 2–3 months? Police certificates move slowly. Banks require special requests. If you have multiple income sources, verification takes longer.

**Month 2–3: Consulate Appointment Booking**

Once you've gathered everything, you submit a "pre-application" to your consulate (Spain's weird—some consulates call this different things). They review and give you an appointment date.

This is where it gets frustrating: appointment slots book out months in advance in some cities. London, Madrid, Barcelona often require 8–12 week wait times.

**Month 3–4: The Interview**

You go to your consulate, hand in your papers, answer questions about your income and intent to live in Spain. Most people are in and out in 15 minutes.

**Month 4–5: Decision and Visa Issuance**

The consulate reviews your file. Most approvals come within 6 weeks of interview. Some take up to 12 weeks. It depends on volume and whether they ask for clarification on anything.

Once approved, your passport goes to Madrid for visa sticker. You pick it up from the consulate (usually 1–2 weeks later).

**The Outliers**

- If your income is complex (multiple sources, investments, freelance), expect consulate questions. Add 2–4 weeks.
- If you're applying to a backlogged consulate, the 5-month timeline extends to 6–7 months.
- If something is missing from your paperwork, it gets sent back. Plan for 4 weeks of back-and-forth.

**What This Means for You**

If you start now, realistically you're in Spain on your new visa by Month 5 or 6. Not Month 2. Not Month 9. Around there.

That's not pessimism—that's pattern recognition from 200+ applications.

**Primary CTA:**  
Want to know which consulate has the shortest wait time? [Let's Map Your Path in a Consultation](#).

**Secondary CTA:**  
Still researching? Bookmark this email.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 4 — Day 7 (Branches A & B)
**Goal:** Reduce friction through specificity, build credibility, make action feel simple.

**Subject Line:**  
3 Documents You'll Need (and No, You Don't Have Them Yet)  
*A/B Alternative:* The Document Checklist: What Gets People Stuck

**Preview Text:**  
Most people gather the wrong stuff first. Here's exactly what to request.

**Body Copy:**

Hi [First Name],

We've noticed something: 80% of people applying for the NLV visa gather documents in the wrong order. They spend 3 weeks collecting stuff that isn't even needed, then scramble when they realize they're missing the real requirements.

Let's save you that frustration.

**Document 1: Bank Statements (The Non-Negotiable)**

You need 12 consecutive months of bank statements showing your passive income or pension deposits. Most people think any bank statement works. It doesn't.

What your consulate actually needs:
- Statements showing monthly income deposits (pension, interest, dividends, transfers from abroad)
- Balance sufficient to cover living expenses
- No massive red flags (unexplained deposits, frequent cash withdrawals)

**How to Get It:** Contact your bank directly. Ask for "officially certified bank statements for visa application purposes." Some banks charge €10–20 per statement. Plan 1–2 weeks for delivery.

**Document 2: Proof of Income (The One People Get Wrong)**

This is where it gets consulate-specific. What "proof" means varies wildly.

If you're on a pension:
- Pension statement from your government/provider showing monthly amount
- Recent letter from the pension provider confirming it's ongoing

If you're self-employed or have investment income:
- Last 2 years of tax returns
- Latest brokerage or investment statement
- If freelance: contracts showing ongoing client relationships

If you're employed:
- Employment contract
- Recent payslips
- Letter from employer confirming ongoing employment

**Why it's tricky:** Each consulate has slightly different requirements. Some accept digital copies. Others don't. Some want certified translations; others don't. This is where people waste 4 weeks going back and forth.

**Document 3: Police Certificate (The Time Sink)**

You need a clean police record from your country of origin. Sounds simple. It's not.

- US: Takes 4–8 weeks from FBI
- UK: Takes 2–4 weeks from Disclosure and Barring Service
- Canada: Takes 2–6 weeks from local police
- Australia: Takes 2–3 weeks from Australian Federal Police

Order this first. You'll need the original or officially certified copy, and most consulates want no translations (they use court-appointed translators instead).

**The Order That Works**

1. Request police certificate (it takes longest)
2. While you're waiting, contact your bank for statements
3. While you're waiting for those, gather proof of income (tax returns, pension letters)
4. By the time everything arrives, you're ready to submit

Total action on your part: 3–4 hours over 2 weeks.

**Primary CTA:**  
Want us to send you the exact email templates to request each document from your bank and government? [Book a consultation](#) and we'll give them to you.

**Secondary CTA:**  
Already gathering? Use the list above as your checklist.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 5 — Day 10 (Branches A & B)
**Goal:** Build emotional trust, differentiate service, lower perceived risk of moving forward.

**Subject Line:**  
Why People Hire Us (Spoiler: It's Not What You'd Expect)  
*A/B Alternative:* The Real Reason Clients Choose Us Over DIY

**Preview Text:**  
It's not about the paperwork. It's about what we know that they don't.

**Body Copy:**

Hi [First Name],

We ask every client: "What made you decide to hire us instead of doing this yourself?"

The answers are always the same, and they're never about price.

**"My Consulate's Approval Rate is 67%, and I Didn't Know That"**

Some consulates approve 9 out of 10 visa applications. Others approve 6 or 7 out of 10. Why? Different people reviewing files. Different interpretation of rules. Different strictness on document standards.

When we help you, we already know your consulate's approval rate, common rejection reasons, and what they obsess over. You walk in prepared.

**"I Didn't Know That Income Source Didn't Count"**

Rental income, interest from certain accounts, gifts from family—the rules on what counts toward the €28,800 are specific and not obvious. One client was planning to use rental income she thought "didn't count." We caught it in a 10-minute conversation. She restructured, saved 3 months of back-and-forth.

**"I Would've Submitted Incomplete Paperwork"**

This happens constantly. Someone submits 9 out of 10 required documents, the consulate sends everything back, and they lose 2 months. We audit your file before you walk into that appointment.

**"My Consulate Wanted a Specific Format, and I Wouldn't Have Known"**

Barcelona's visa unit wants bank statements in a specific format. Madrid doesn't care. Someone applying in Barcelona without knowing this would submit the "wrong format" (which isn't actually wrong, just different), causing delays.

We know these quirks for every consulate in Europe.

**"I Didn't Want to Call My Bank 6 Times"**

Getting a bank to issue officially certified statements is annoying. Getting them translated is more annoying. Getting them in the exact format the consulate wants is a whole thing. We've written the templates. We know which banks are responsive. We know the translators who work fast.

So you make one phone call instead of six.

**The Pattern**

It's never about us doing the paperwork for you (though we can). It's about us knowing what's actually going to work and what's going to get sent back.

We've done this 200+ times. You're doing it once. That difference is worth something.

**Primary CTA:**  
Let's talk about whether we're a fit for what you need. [Book a 30-minute consultation](#).

**Secondary CTA:**  
Have questions first? Reply to this email.

**Exit Condition:**  
User books consultation → Sequence 3.  
User replies with detailed questions → sales team responds personally.

---

## Email 6 — Day 12 (Branches A, B, C)
**Goal:** Final soft push to consultation booking. Simple, clear, minimal friction.

**Subject Line:**  
Book Your Consultation — 30 Min, Free, This Week  
*A/B Alternative:* Let's Clear This Up (Seriously, It's Fast)

**Preview Text:**  
You've got options. A quick conversation is all you need to know which one is yours.

**Body Copy:**

Hi [First Name],

You've made it through all our educational emails (thanks for sticking with us). Here's the thing: we can answer the rest of your questions in a conversation way faster than over email.

**What a Consultation Looks Like**

- 30 minutes, no pressure
- We walk through your specific situation
- We tell you straight: what's straightforward, what's complex, what timeline is realistic
- You ask any questions you want
- We send you everything we discussed (no follow-up work on your part)

**What You'll Know After the Call**

- Which visa actually fits your life
- What you'll spend in time and money
- Realistic timeline from where you are now to Spain
- Whether working with us makes sense (it might not—and that's okay)

**Open Slots This Week**

[Calendar link if using scheduling software, or:]

Let us know 2–3 times that work, and we'll find a spot.

**A Note if You're in Branch C (Not Eligible Yet)**

If you're not ready now, we get it. But we want to stay in touch. A quick call helps us understand your timeline better so we can reach back out at the right moment—when you actually need us.

No pressure. Just a conversation.

**Primary CTA:**  
[Book Your Free Consultation](#)

**Secondary CTA:**  
Reply with your availability.

**Exit Condition:**  
User books consultation → Sequence 3.  
User unsubscribes → remove from all sequences.  
No action after Email 6 → move to `nurture_only` list, send once monthly, track for re-engagement.

---

# SEQUENCE 2: POST-DOWNLOAD
## Goal: Educate + Build Trust + Convert to Consultation

### Sequence Overview

| Email | Day | Subject | Type | Purpose |
|-------|-----|---------|------|---------|
| 1 | 0 | Your Checklist is Ready + Here's What To Do First | Welcome | Anchor, set expectation |
| 2 | 3 | The Mistake People Make (And How to Avoid It) | Value | Address common pain, build trust |
| 3 | 7 | Your Timeline: From Now to Moving Day | Educational | Paint picture, reduce uncertainty |
| 4 | 12 | Real Costs (So You Know What to Budget) | Value | Transparency = credibility |
| 5 | 17 | Stories From People Like You | Social Proof | Reduce risk perception |
| 6 | 21 | Ready for the Next Step? | CTA | Soft conversion to consultation |

### Branching Logic

**No branching in this sequence.** All users receive the same track regardless of which lead magnet they downloaded (NLV, DNV, or Moving to Spain checklist). Content is general enough to apply to all three, with personalization opportunities noted in copy.

### Send Time Recommendation
- **Email 1 (Day 0):** Immediately upon download (within 1 hour)
- **Emails 2–6:** 9 AM in user's local timezone

### ESP Tags Required
- `seq2_postdownload`
- `magnet_nlv` / `magnet_dnv` / `magnet_moving` (track which checklist was downloaded)
- `engaged_content` (user consumed educational content)
- `consider_consultation` (tag after Email 3)

### KPI Benchmarks
- **Open Rate:** 50–60%
- **Click Rate:** 14–20%
- **Reply Rate:** 2–4%
- **Consultation Booking Rate:** 12–18%
- **Unsubscribe Rate:** <0.8%
- **Forward Rate:** 2–3% (content is shareable)

---

## Email 1 — Day 0
**Goal:** Welcome user, anchor expectations, position next step.

**Subject Line:**  
Your Checklist is Here + What to Do This Week  
*A/B Alternative:* Let's Get Organized (Checklist Inside)

**Preview Text:**  
Download it, bookmark it, and here's what you should do first.

**Body Copy:**

Hi [First Name],

Your checklist is attached (and you'll get a backup link below in case it's easier to access online).

This document took us a while to build. It's based on 200+ visa applications, conversations with 50+ consulates, and feedback from clients who've already moved. It's specific to your visa type, and it's not fluffy.

**Here's How to Use It**

Open it. Skim it. You'll notice sections for documents, timeline, costs, and common questions. Don't try to tackle everything at once.

What most people do (which works):
1. Read the Overview section (5 minutes)
2. Skip to the section that matches where you are now (gathering docs, applying, waiting for approval)
3. Use it as a reference as things move forward

**The Part We Want You to Pay Attention to**

See the "Common Rejections" section? Yeah, that one. We included it because these are the things that get visa applications sent back. Knowing what NOT to do saves months.

**What's Next**

Over the next few weeks, we're sending you some additional context. Nothing overwhelming. Just context on timelines, costs, and what people don't expect.

Some of it will be "oh, I didn't know that." Good—that's the point.

**Primary CTA:**  
[Download Your Checklist](#) (or access it [here](if link))

**Secondary CTA:**  
Have questions? Reply to this email. We read everything.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 2 — Day 3
**Goal:** Address common pain point, position as expert, build trust through specifics.

**Subject Line:**  
The Biggest Mistake We See (And How to Avoid It)  
*A/B Alternative:* Why 1 Out of 4 Applications Get Rejected

**Preview Text:**  
It's not what you'd expect. We caught it for you.

**Body Copy:**

Hi [First Name],

We're going to tell you the thing that gets visa applications rejected more than anything else.

Ready?

**The Mistake: Inconsistent or Vague Proof of Income**

Here's what happens:
1. Someone gathers bank statements showing monthly deposits.
2. But the deposits are labeled "transfer from abroad" or "income" with no source.
3. Or the deposits are inconsistent—€1,200 one month, €1,500 the next, then nothing for 6 weeks.
4. Or they show savings, but not actual ongoing income.

The consulate receives the file and thinks: "We can't verify this is real income. We can't verify it's ongoing. Rejected. Reapply with clarification."

6 weeks lost. Application bounced back.

**Why It Happens**

Most people don't think about how their income looks on a bank statement. They think about what they *know* is true. Those aren't the same thing.

Example: You get a pension from your home country. You know it's real and ongoing. But on your Spanish bank statement, it appears as one monthly deposit with a label like "International Transfer." Without documentation explaining what that deposit is, the consulate can't verify it.

Another example: You have investment income. You know you receive it regularly. But your account shows deposits from your brokerage with a vague label, and the amounts vary slightly based on performance. The consulate can't tell if this is reliable ongoing income or just account activity.

**How to Avoid It**

When you gather your financial documents, don't just get bank statements. Get:

1. **A letter from your income source** (pension provider, employer, investment company) that states:
   - The type of income
   - The monthly or annual amount
   - That it's expected to continue
   - The date it started

2. **Annotate your bank statements** (not by hand—in a document you prepare) with notes like:
   - "Monthly pension from [Pension Provider]"
   - "Quarterly dividend from [Brokerage]"
   - "Monthly salary from [Employer]"

3. **Show the bank statement label clearly** so it matches the supporting letter.

This takes 2 hours of your time. It prevents 6 weeks of delays.

**What We Do Differently**

When we review someone's file before they submit, we spot this immediately. "Your income looks good, but your consulate won't be able to verify it." Then we help them get the letters and docs they need.

It's not complicated. It's just knowing what "proof" actually means to a government office.

**Primary CTA:**  
Check your checklist—we included a section on "Proof of Income: Getting It Right." Review it this week.

**Secondary CTA:**  
Not sure if your documents will pass the sniff test? [Let's talk](#)—we can audit them before you submit.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 3 — Day 7
**Goal:** Paint a picture of the process, reduce uncertainty, build anticipation for the move.

**Subject Line:**  
Your Timeline: From Now to Moving Day (Month by Month)  
*A/B Alternative:* The Actual Calendar: When You'll Be in Spain

**Preview Text:**  
Here's when everything happens, so you can plan the rest of your life.

**Body Copy:**

Hi [First Name],

You've downloaded the checklist. You're thinking about timelines. Let's map it out so you can actually plan.

We're going to assume you're starting from scratch this month. If you've already started, adjust the dates back.

**Month 1: Gathering**

- Week 1–2: Order your police certificate. (Seriously, do this first. It's the time sink.)
- Week 2: Request 12+ months of bank statements from your bank. Specify they need to be "officially certified for visa application purposes."
- Week 2–3: Request proof of income documents from your pension provider, employer, investment company, etc.
- Week 3–4: Collect other docs you need (passport copies, travel history, accommodation proof in Spain).

**What You're Actually Doing:** One email to your bank, one call to your pension provider, maybe a reply to an employer. Total action: 3–4 hours spread across 4 weeks.

**End of Month 1 Status:** Police certificate is on its way. Bank statements in-hand or arriving soon. Most other docs gathered.

---

**Month 2: Organizing and Pre-Screening**

- Week 1–2: Receive or chase down remaining docs.
- Week 2–3: Organize everything, make copies, get any translations done (if required by your consulate).
- Week 3–4: Prepare cover letter explaining your application and address in Spain.

**What You're Actually Doing:** Putting documents in a folder. Making photocopies. Maybe translating a document or two (depends on your consulate). Total action: 4–6 hours.

**End of Month 2 Status:** You've got everything. You're ready to apply.

---

**Month 3: Submitting**

- Week 1–2: Contact your consulate to schedule your pre-application appointment (they review docs before you come in).
- Week 2–4: Submit your file (either online, by mail, or in person depending on consulate).

**What You're Actually Doing:** Upload files to a portal or mail them to an address. One phone call to confirm receipt.

**End of Month 3 Status:** Your application is in the system. You're now waiting.

---

**Month 4: Waiting**

This is the frustrating part. You've done everything. The consulate has your file. They're reviewing it. You're checking your email daily hoping for an appointment notice.

- Week 1–2: Consulate might ask clarification questions. You respond quickly.
- Week 2–4: Most likely, silence. They're just reviewing.

**What You're Actually Doing:** Possibly respond to one email. Otherwise, nothing. You're waiting.

**End of Month 4 Status:** Consulate sends you an interview appointment (usually 2–4 weeks out).

---

**Month 5: Interview and Approval**

- Week 1–2: You attend your visa interview at the consulate (usually 15 minutes).
- Week 2–4: Consulate issues decision. Most approvals come within 2–3 weeks. Rejections are rare if your paperwork was solid.

**What You're Actually Doing:** Show up at consulate, answer questions ("What's your plan in Spain?", "How will you spend your days?", "Where will you live?"). Hand over your passport.

**End of Month 5 Status:** You're approved. Your passport is with the consulate being prepped for visa sticker. It'll be ready for pickup in 1–2 weeks.

---

**Month 5–6: Final Steps**

- Week 1–2: Receive notification that your visa is ready. Pick up passport from consulate.
- Week 2: You have your visa. You can book travel and give notice to your current landlord/employer.

**Your Reality Check**

This is 5–6 months if:
- You're organized
- Your consulate isn't backlogged
- Your paperwork is clean
- They don't ask follow-up questions

In a normal scenario with a few hiccups (consulate delays, slow bank, paperwork goes missing once), add 2–4 weeks.

**The Part People Miss**

Once you have your visa, that's not the end. You still need to:
- Arrange housing in Spain
- Book travel
- Handle logistics (healthcare registration, bank account, tax ID)

That's another 2–4 weeks of logistics. So realistically, from visa in hand to actually living in Spain: 4–6 weeks more.

**Total: 6–7 months from "I'm thinking about this" to "I'm living in Spain."**

**Primary CTA:**  
Use this timeline to plan backwards. When do you want to be in Spain? That tells you when to start applying.

**Secondary CTA:**  
Want to map out your specific timeline? [We can show you](#) exactly when things happen for your consulate.

**Exit Condition:**  
User books consultation → Sequence 3.  
Tag user with `consider_consultation` for future targeting.

---

## Email 4 — Day 12
**Goal:** Remove financial uncertainty, build transparency, position costs as reasonable.

**Subject Line:**  
Real Costs: What You'll Actually Spend (No Surprises)  
*A/B Alternative:* The Budget Breakdown: What Spain Visa Applications Actually Cost

**Preview Text:**  
The visa fee is cheap. Everything else? Let's talk about it.

**Body Copy:**

Hi [First Name],

People ask us: "How much is this going to cost?" They usually expect one number. It's more nuanced than that.

Let's break it down.

**The Visa Fee Itself**

Spain charges €84 for a Non-Lucrative Visa (or €116 if you're applying from outside Spain's jurisdiction). That's it. That's the official government fee.

**Everything Else**

Here's where costs vary based on your situation:

**Police Certificate**  
- US: Free–$25 (depends on state)
- UK: £13
- Canada: Free–$25
- Australia: Free–$50
- Translation (if needed): $20–60

**Bank Statements and Financial Documents**  
- Official certified statements: €5–20 per consulate (varies by bank)
- Total across 12–24 statements: €60–240
- Translation: $30–100

**Medical Exam** (required for DNV visas, optional for NLV)  
- Private clinic: €50–150 (depends on city and extent)

**Translation of Documents**  
- DIY (if you speak Spanish): Free
- Certified translator: €0.15–0.30 per word
- Example: translating 10,000 words (average for full visa file) = €1,500–3,000
- Budget: $500–2,000 depending on number of docs

**Consulate Appointment** (if you need to go in person)
- Some consulates waive this. Others don't.
- If required, you're likely doing it by mail or online anyway: Free

**Travel to Consulate** (if required)
- If you're applying in-person: flights, hotels, meals = varies wildly
- Most people do this by mail or appointment waiver: $0–500+

**NIE Application** (once you arrive in Spain)
- Free (Spanish tax ID number)
- You handle this after visa is approved

**Accommodation Deposits and Setup**
- Not part of visa cost, but part of moving cost
- Budget: €1,500–3,000 for first month + deposit

**Total DIY Costs**

- Budget: €1,500–3,500 ($1,600–3,800 USD)
- If you need heavy translation: €2,500–5,000+

Most of this is paid upfront (first 2 months). The visa fee itself? €84. Everything else is supporting services and logistics.

**Why People Spend More**

1. **Rush translation services:** You wait too long, panic, and pay extra for 48-hour turnaround. Plan ahead, save money.

2. **Multiple consulate visits:** You miscalculate and have to travel twice. Once is usually enough.

3. **Fixing errors:** You submit incomplete docs, they get rejected, you spend money resubmitting. Getting it right the first time saves €500–1,000.

4. **Professional help:** If you hire someone to handle application, translation, and consulate coordination, add €1,500–4,000.

**Our Value (Being Honest)**

If you use our service, you're paying us a fee. That cost is separate from what Spain charges. Why?

- We do the consulate-specific troubleshooting (saves you 40–60 hours of research and back-and-forth)
- We audit your documents before submission (catches mistakes that would cost you €500–1,000 in delays and resubmission)
- We handle translator coordination (we know the good ones, saves time and often saves money)
- We've done this 200+ times; you're doing it once. That expertise has value.

Whether DIY or professional, most people spend €1,500–7,000 to move to Spain legally. It's not cheap, but it's not a huge amount relative to moving itself.

**Primary CTA:**  
Curious what our service costs? [Let's talk about your specific situation](#). Every file is different.

**Secondary CTA:**  
Still in research mode? Bookmark this email for budgeting.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 5 — Day 17
**Goal:** Build credibility through social proof, reduce perceived risk, humanize the brand.

**Subject Line:**  
Stories From People Like You (Who Are Now in Spain)  
*A/B Alternative:* What 5 Clients Told Us After Moving

**Preview Text:**  
"I thought this would be way harder." Here's what actually happened.

**Body Copy:**

Hi [First Name],

We asked some recent clients: "What surprised you most about the visa process?"

Here's what they said.

---

**"The Paperwork Was Less Scary Than I Expected"**

*— Sarah, UK, NLV Visa, Moved to Barcelona 8 weeks ago*

"I was dreading this. I thought I'd have to translate 500 documents and deal with endless bureaucracy. Turned out, the actual list was shorter than I expected, and most of it was just organizing stuff I already had.

The part that helped: someone telling me exactly what I needed before I started gathering. I didn't waste time on things that didn't matter."

---

**"My Consulate Wanted a Specific Format, and I Would've Screwed It Up"**

*— Michael, Australia, DNV Visa, Moved to Madrid 4 months ago*

"My consulate's website was vague. I found out later they have unwritten rules about how documents should be submitted. I would have submitted my file and gotten rejected.

Knowing those rules in advance (because someone had already dealt with that same consulate) saved me 2 months and a lot of frustration."

---

**"The Waiting Part Was Worse Than I Expected"**

*— Jen, Canada, NLV Visa, Moved to Valencia 3 months ago*

"Once I submitted, I just... waited. For weeks. I kept refreshing my email. I thought something was wrong. Turns out, the consulate is just slow. Nothing was wrong; they were just reviewing.

Having a realistic timeline helped me not panic. I set an expectation in my head: 'This will take 4–6 weeks. Until then, do something else.' Made a huge difference."

---

**"I Didn't Realize How Flexible I Could Be on Logistics"**

*— David & Lisa, US, NLV Visa, Moved to Seville 6 weeks ago*

"We thought we had to have a place lined up, a job, a plan. Turns out, the visa doesn't care. The consulate just wants to know you have income and won't be a burden. Where you live and what you do with your days is flexible.

That freed us up. We moved with a provisional rental, took our time finding the right place, and aren't stressed."

---

**"Hiring Help Was Worth It"**

*— Rachel, South Africa, NLV Visa, Moved to Malaga 2 months ago*

"I didn't want to deal with this myself. I'm not detail-oriented by nature. I knew I'd lose paperwork or miss something. Paying someone to handle it was worth the peace of mind.

I just answered questions, they handled everything else. Felt simple."

---

**The Pattern**

Most people expect this to be:
- Harder and more expensive than it is (it's often simpler)
- Slower than it is (if organized, it moves)
- Scarier than it is (government is just slow, not mean)

The difference between people who say "glad that's over" vs. "that was stressful" usually comes down to knowing what to expect and when.

**Your Move**

You're at the stage where you're researching. You're smart for doing that. The next stage is testing whether your situation is actually straightforward (spoiler: most people's are).

That's what the consultation is for.

**Primary CTA:**  
[Book a conversation with us.](#) 30 minutes. We'll tell you straight whether your path is simple or complex.

**Secondary CTA:**  
Have more questions? We're reading all replies.

**Exit Condition:**  
User books consultation → Sequence 3.

---

## Email 6 — Day 21
**Goal:** Final soft CTA, low-pressure, acknowledge different personas (DIYers vs. outsourcing).

**Subject Line:**  
Ready for the Next Step? (You Know What to Do)  
*A/B Alternative:* You've Got Everything You Need — Or Do You?

**Preview Text:**  
Some people DIY this. Some get help. Both are fine. Let's figure out which is you.

**Body Copy:**

Hi [First Name],

You've read our emails. You've got the checklist. You've heard from people who've done this. You know the timeline, the costs, and the common mistakes.

At this point, you probably fall into one of three buckets:

**Bucket 1: "I've Got This, Going to DIY"**

Cool. You're organized, you like researching, you don't mind a few back-and-forth emails with your consulate. You'll get there. The checklist and everything we've sent you is enough to not step on a rake.

(Bookmark our emails for reference as you move through the process. And if you hit a wall later, you know where we are.)

**Bucket 2: "This Seems Complicated, I Want Help"**

Also cool. This is exactly what we do. Some people want someone else worrying about whether their translation format is correct, whether their consulate has specific rules, whether their income documentation will actually work.

If that's you, let's talk. 30 minutes. We'll see if we're a fit for what you need.

**Bucket 3: "I'm Still Thinking About It"**

No pressure. This isn't a now-or-never decision. You can revisit this in 3 months. We'll still be here. You'll still have the checklist. When you're ready to move forward, reach out.

**What We're Not Doing**

We're not going to hammer you with emails about your uncertainty. We're not going to spam you with "last chance" messages. (That's annoying and it doesn't work.)

We're here. You know who we are. When you're ready to move forward—whether that's next week or next year—you know where we are.

**If You Want to Talk**

[Book a consultation.](#) No obligation. Just a conversation.

**If You Want to Keep Reading**

We send occasional emails about moving to Spain, visa updates, and real-life stuff that's not super salesy. If you want to stay in that loop, you're already on it.

**Primary CTA:**  
[Ready? Let's Talk](#)

**Secondary CTA:**  
Reply to this email anytime. We read everything.

**Exit Condition:**  
User books consultation → Sequence 3.  
User unsubscribes → remove from all sequences.  
No action after Email 6 → move to `segmentation_list_postdownload`, send monthly educational content, monitor for re-engagement over 6 months.

---

# SEQUENCE 3: POST-CONSULTATION
## Goal: Close to Paid Engagement / Retain / Collect Testimonial

### Sequence Overview

| Email | Day | Subject | Branch | Purpose |
|-------|-----|---------|--------|---------|
| 1 | 0 | Thanks for Today + Here's What We Discussed | Both | Recap + anchor next steps |
| 2 | 2 | [BRANCH A] You're Signed Up — Here's Your First Steps | Client | Onboard + confirm engagement |
| 2 | 2 | [BRANCH B] One Thing We Want to Revisit | Non-Client | Soft re-engagement |
| 3 | 7 | Your Month-by-Month Roadmap | Both | Clarity, reduce overwhelm |
| 4 | 17 | How We Handle This (From File Setup to Interview) | Client | Demonstrate value, build confidence |
| 4 | 17 | Success Stories: Where People Got Stuck (and How) | Non-Client | Gentle push, address concerns |
| 5 | 30 | Next Steps — What Happens Now | Both | Transition + retention check |

### Branching Logic

**Branch A: Became a Client**  
User signed up for paid service during/immediately after consultation. Path: onboarding, confidence-building, deliver value, establish communication cadence.

**Branch B: Did Not Yet Commit**  
User had consultation but didn't commit to paid service. Path: soft re-engagement, address remaining objections, offer alternative entry points (if available), stay warm for future conversion.

### Send Time Recommendation
- **Email 1 (Day 0):** Within 4 hours of consultation call end
- **Emails 2–5:** 10 AM in user's local timezone (after they've had morning coffee, before too busy)

### ESP Tags Required
- `seq3_postconsult`
- `client_onboarding` (Branch A) / `prospect_nurture_warm` (Branch B)
- `ready_for_next_call` (tag after Email 3 if no engagement)
- `testimonial_candidate` (tag after Email 4 if client, after Email 5 if non-client who didn't book)

### KPI Benchmarks
- **Open Rate:** 65–75% (high engagement expected)
- **Click Rate:** 18–25%
- **Reply Rate:** 8–15%
- **Client Retention Rate:** 90%+ (week 4 check-in)
- **Testimonial Collection Rate:** 40–50% (from paying clients at week 4–6)
- **Non-Client Re-engagement Rate:** 15–25% (converts back to consultation or new booking)

---

## Email 1 — Day 0
**Goal:** Thank user, recap call, clarify next steps, remove decision anxiety.

**Subject Line:**  
Thanks for Today — Here's What We Discussed  
*A/B Alternative:* Recap: Your Visa Path + What's Next

**Preview Text:**  
We said a lot. Here's what matters. And next steps.

**Body Copy:**

Hi [First Name],

Great talking with you today. We know we covered a lot—timelines, documents, consulate quirks, costs. We want to recap the key points so nothing gets lost in the shuffle.

**Your Visa Path**

You're applying for the [NLV / DNV / Other] visa. You're applying to the [Consulate/City] consulate. Your earliest realistic start date is [Month]. Your estimated timeline is [X months].

**What Makes Your Application Straightforward**

[Based on call: income is clear, docs are gathered, consulate has fast approval rate, etc.]

**What We'll Need to Pay Attention To**

[Based on call: this consulate is specific about formatting, you have multiple income sources (doable but needs careful documentation), you need to gather X particular doc, etc.]

**Estimated Cost Breakdown**

- Government fees: €84
- Document preparation/translation: [€X range]
- [If applicable: Our service fee for [scope of work]: €X]
- Total estimated: €[range]

**Next Steps**

[If Branch A — Became Client:]  
You've signed up with us. Here's what happens next:
- You'll receive a welcome email with your client portal access within 24 hours
- We'll send you a detailed intake form (takes 20 minutes to complete)
- Once we get that back, we'll build out your document checklist and timeline
- Our first milestone check-in is [date]. We'll review what you've gathered so far

[If Branch B — Did Not Yet Commit:]  
We gave you some stuff to think about. If you want to move forward—whether with us or on your own—here's the best way to reach us:
- Reply to this email anytime
- Book another call if you want to explore further
- Check back in 2 weeks and let us know how the research is going

**What We Need From You**

[If Branch A:]  
1. Check your email for the portal access (look for subject: "[Your Name] — Your MSV Client Portal")
2. Fill out the intake form
3. Reply to this email if you have questions about anything we discussed

[If Branch B:]  
1. Think about what's still unclear
2. Start gathering one category of documents (if you want to get a head start)
3. Reply to this email if something comes up or you want to revisit the conversation

**A Note on What We Won't Do**

We won't pressure you. We won't send daily emails. We won't make this weird. We'll stay in touch, we'll be useful, and if you decide to work with us later, great. If you don't, also fine—we'll still send you occasional useful stuff because we believe in helping people move to Spain.

**Primary CTA (Branch A):**  
[Access Your Client Portal](#)

**Primary CTA (Branch B):**  
[Book Another Conversation](#) if you want to dig deeper.

**Secondary CTA (Both):**  
Reply to this email with any immediate questions.

**Exit Condition:**  
User signs up for service → continue Branch A emails.  
User declines service → continue Branch B emails.  
User unsubscribes → remove from all sequences.

---

## Email 2 — Day 2 (Branch A: Became Client)
**Goal:** Confirm engagement, set expectations, deliver immediate value, celebrate decision.

**Subject Line:**  
You're All Set — Here's Your First Move  
*A/B Alternative:* Welcome to Your Visa Journey (Let's Get Organized)

**Preview Text:**  
Portal is live. Start here. We'll take it from there.

**Body Copy:**

Hi [First Name],

Welcome. You're now set up in our system. Here's what's happened on our end and what happens next.

**What We've Done**

- Created your file with all the notes from our conversation
- Built your document checklist specific to your consulate
- Mapped your timeline with key milestones
- Flagged the items we know your consulate is picky about

All of that is now in your portal.

**What You Need to Do (This Week)**

1. **Log into your portal** [link]. Check your email for login credentials.

2. **Review your personalized checklist.** It's different from the generic one you downloaded. This one is built just for your situation and your consulate. Skim it. You don't need to action everything today.

3. **Reply to this email with one thing:** What's the first document you're going to gather? (Usually: police certificate, because it takes the longest.) Just tell us which one, and we'll know you're moving.

That's it for now. Three tiny things.

**What Happens Next**

- **Week 1–2:** You'll start gathering documents. We're here to answer questions as they come up.
- **Week 2–3:** You'll upload documents to your portal as you gather them. We'll review and flag anything that looks off.
- **Week 3–4:** First milestone check-in. We jump on a quick call to review what you've got and what's still pending.

**Why We Do It This Way**

You're not paying us to hold your hand. You're paying us to be expert reviewers who catch mistakes before they become expensive. So: you gather, we review, we catch issues early, you move forward with confidence.

**Why You Made the Right Choice**

I'm going to be honest: you could do this yourself. Some people do. They save money. They also spend 40+ hours researching, they're never quite sure if they're doing it right, and some of them (not all, but some) hit snags that cost them 2 months and €500+ to fix.

What you're paying us for is:
- Not having to worry
- Knowing what your consulate actually cares about
- Having someone catch mistakes before they're expensive
- A clear process instead of scattered research

That's worth something to most people. Apparently it was worth something to you too, and we're glad.

**What You Can Expect From Us**

- Reasonable response time (24 hours during business days)
- Straight talk (if something is an issue, we'll tell you)
- No surprises (you'll know the timeline, costs, and what's needed)
- Actual expertise (we've done this 200+ times)

**The Thing We Always Mention**

This process is linear but not always smooth. Some consulates are slow. Some docs take longer than expected. That's normal. When something happens, you hear from us immediately. You don't stress in silence.

**Primary CTA:**  
[Log Into Your Portal](#) and start with that checklist.

**Secondary CTA:**  
Reply with the first document you're gathering.

**Exit Condition:**  
User engages with portal → send weekly engagement emails.  
User doesn't engage within 7 days → send gentle nudge email.

---

## Email 2 — Day 2 (Branch B: Did Not Yet Commit)
**Goal:** Soft re-engagement, address unspoken objections, leave door open, demonstrate value.

**Subject Line:**  
One Thing We Want to Revisit From Our Conversation  
*A/B Alternative:* We Thought of Something Else You Should Know

**Preview Text:**  
It might change your thinking. Or it might not. Either way, worth knowing.

**Body Copy:**

Hi [First Name],

After our conversation today, we realized there's one thing we should have dug deeper on, and we want to address it now.

**The Thing**

[Based on your call: You seemed concerned about X / You weren't sure if Y applied to you / You were quiet when we mentioned Z / You said you wanted to think about whether to DIY or get help]

Here's the actual situation:

[Clarify the objection directly. Be helpful. Don't be salesy. Examples:]
- "You said you're worried about cost. Here's the reality: even if you DIY, you'll spend €1,500–3,000. Our service costs €[X]. The difference is paying us to not stress about whether you're doing it right."
- "You seemed unsure whether your income would count. We've seen exactly your situation before. It counts. Here's why. It's straightforward."
- "You said you have time and want to DIY. That's totally fair. If you hit a wall in 4 weeks, you know where we are."

**Why We're Bringing It Up**

We don't want you to make a decision based on incomplete info or worry that might not be necessary. You can disagree with us and DIY—that's fine. But you should decide based on facts, not fear.

**Your Options**

1. **DIY:** You've got the checklist and our emails. You know what to do. It'll take 40–60 hours of your time, but you'll get there. (And if you get stuck, we do accept new clients mid-process; it's just more complicated.)

2. **Outsource to us:** You pay our fee. We handle the consulate knowledge, the document review, the timeline management. You just gather docs and show up for your interview.

3. **Hybrid:** You gather some docs, we review them and guide the rest. Not all firms do this, but we can. Less expensive than full service, but you get expert eyes on your application.

4. **Keep researching:** That's also fine. You know where we are when you're ready.

**The Only Wrong Answer**

Trying to DIY this while stressed and unsure. That's when people miss things.

**Primary CTA:**  
Reply to this email and tell us which option is appealing. No commitment. Just conversation.

**Secondary CTA:**  
[Book another call](#) if you want to explore the hybrid or outsource options more.

**Exit Condition:**  
User books another call → restart Sequence 3 from Email 1 with updated content.  
User replies with questions → sales team responds personally.  
No engagement after Email 5 → move to `prospect_nurture_warm` for monthly touchpoint.

---

## Email 3 — Day 7 (Both Branches)
**Goal:** Paint concrete picture, reduce overwhelm, show structure and process, build confidence.

**Subject Line:**  
Your Month-by-Month Roadmap (What Happens When)  
*A/B Alternative:* The Actual Timeline: Month by Month, Step by Step

**Preview Text:**  
Here's the structure. Nothing ambiguous. Just what's next.

**Body Copy:**

Hi [First Name],

One of the biggest sources of stress in this process is not knowing what's supposed to be happening and when. We're going to fix that right now with your personalized roadmap.

**Your Specific Timeline**

[Based on call:]  
- **Start Month:** [Month when user starts gathering docs]
- **Consulate:** [City/Consulate Name]
- **Estimated Approval Timeline:** [If fast consulate: 4–5 months; if slow: 6–8 months]
- **Target Visa-in-Hand Date:** [Month/Year]

**Month 1: Gathering + Organizing**

**Your Immediate Actions (This Week)**
- Order police certificate (first thing, takes longest)
- Request 12+ months bank statements from your bank
- Reach out to [income source] for proof of income letter

**Our Action**  
- Review as you gather
- Flag if anything looks like it won't pass consulate review
- Clarify consulate-specific requirements

**By End of Month 1**  
You have: police certificate in-hand or arriving, bank statements, proof of income, other core docs organized.

**Milestone Check-in**  
[If Branch A — we'll call on [date] to review; if Branch B — let us know how this is going]

---

**Month 2: Final Prep + Submission**

**Your Actions**
- Gather any remaining documents
- Get translations done (we'll tell you which docs need translation based on consulate)
- Organize everything in the order your consulate wants

**Our Action**  
- Final review of your complete file
- Make sure nothing is missing
- Prepare cover letter explaining your application

**By End of Month 2**  
You're ready to submit. Everything is checked.

**Risk Check**  
Before you submit, we do a final scan: "Is this going to get approved, or is there something the consulate will ask about?" If there's any doubt, we tell you.

---

**Month 3: Submission**

**Your Action**  
- Submit application per your consulate's process (online portal, mail, or in-person appointment)

**Our Action**  
- Confirm receipt
- Track with consulate (some consulates are receptive; some aren't)
- Keep you updated

**By End of Month 3**  
Application is in the system.

---

**Month 4–5: Review + Interview**

**Your Action**  
- Wait (hardest part)
- Respond to any consulate questions if they come up

**Our Action**  
- Respond to consulate questions on your behalf (if you want us to)
- Keep you from panicking (nothing news is usually good news)
- Book your interview when appointment comes through

**By End of Month 5**  
You've had your interview. Decision is coming.

---

**Month 5–6: Approval + Pickup**

**Your Action**  
- Pick up your visa from consulate when notified
- Book your travel

**Our Action**  
- Celebrate with you
- Give you guidance on next steps (what to do when you arrive in Spain)

**By End of Month 6**  
You have your visa. You're ready to move.

---

**What This Means**

You're looking at 5–6 months from where you are now to visa in hand, assuming:
- You stay organized
- Your docs are clean
- Consulate doesn't ask surprise questions

If there are hiccups (and sometimes there are), add 2–4 weeks.

**What Doesn't Change**

The timeline is what it is. You can't speed it up by being anxious. You can speed it up by being organized and not missing deadlines.

**Primary CTA:**  
[If Branch A:] Use this roadmap to plan your personal move (housing, job, logistics).

[If Branch B:] Keep this timeline. It's the realistic one. Use it to decide whether to outsource or DIY.

**Secondary CTA:**  
Reply if you see something in the timeline that doesn't match your situation.

**Exit Condition:**  
[Branch A:] User stays engaged → continue with Email 4.  
[Branch B:] User books consultation → restart from Email 1.  
No engagement → monitor.

---

## Email 4 — Day 17 (Branch A: Client)
**Goal:** Deliver value, demonstrate expertise, build confidence in the partnership, show behind-the-scenes.

**Subject Line:**  
How We Handle This (From File Setup to Interview)  
*A/B Alternative:* Behind the Scenes: What We Do That You Don't See

**Preview Text:**  
Here's the actual work that makes the difference.

**Body Copy:**

Hi [First Name],

You've signed up with us. You know the timeline. You might be wondering: "What exactly are you doing to earn this fee?"

Fair question. Let's be specific.

**Document Verification**

When you upload documents to your portal, here's what happens:
- We check each document against your consulate's specific requirements
- We verify bank statements show income the way your consulate expects to see it
- We check for common rejections (inconsistent income, vague labels, missing certifications)
- If we see an issue, we tell you immediately: "This needs to be redone" or "We need to get a supplemental letter from your bank"

This catches mistakes before they're expensive.

**Consulate Research**

Every consulate has quirks. They're not published. We know them because we've worked with them repeatedly.

We know:
- Which consulates accept digital copies, which demand originals
- Which consulates want documents in a specific order
- Which consulates ask the same follow-up questions to everyone (and what that means)
- Which consulates have backlogs and which move fast
- Which translators they recommend (and which they'll reject)
- Which consulates don't require translations that Spain says are "official"

This is the gap between DIY and outsourcing. DIY people find this out the hard way. You don't.

**Timeline Management**

We track your milestones. If you're slow gathering documents and your timeline is slipping, we tell you. If the consulate goes silent for too long, we know whether that's normal or concerning.

We also manage expectations. If your consulate is backlogged, we tell you: "This is a 7-month process, not 5." If it's usually fast, we say: "You'll be approved by Month 5."

**Consulate Communication**

When your application is submitted, we:
- Track it with the consulate (call or email to confirm receipt)
- Respond to any consulate questions on your behalf (if you authorize us)
- Push for clarification if they're unclear about what they need
- Keep you in the loop without stressing you out

**Interview Prep**

Week of your consulate interview, we:
- Send you a guide of likely questions (based on your consulate's style)
- Do a mock interview with you if you want
- Tell you what documents to bring
- Tell you what NOT to overthink (because most interviews are straightforward)

**Cover Letter**

We write your cover letter for you. It explains your financial situation, your intention to live in Spain, and addresses any potential concerns the consulate might have.

This is 2 pages that frame your entire application. It matters.

**The Intangible Stuff**

Honestly, a lot of what you're paying for is peace of mind. You're not worrying about whether you're doing this right. You're not up at 2 AM googling "what if my bank statement looks like this." You're not panicking when the consulate doesn't email you for 3 weeks.

We're worrying. That's the job.

**What This Actually Costs**

Our service fee covers all of this. It's not cheap, but it's less expensive than hiring a full immigration lawyer. And we're more focused than a lawyer—we know exactly what your consulate needs; a lawyer knows the law broadly.

**Primary CTA:**  
Any questions on what's included? Reply to this email.

**Secondary CTA:**  
Ready to start uploading documents? Jump back to your [portal link].

**Exit Condition:**  
User stays engaged → monitor for next milestone.  
Tag as `testimonial_candidate` for later collection.

---

## Email 4 — Day 17 (Branch B: Non-Client)
**Goal:** Gentle push, address remaining concerns, offer alternative entry points, maintain warmth.

**Subject Line:**  
Success Stories: Where People Got Stuck (and How)  
*A/B Alternative:* What We See People Struggle With Most

**Preview Text:**  
These are the moments when people usually call us.

**Body Copy:**

Hi [First Name],

We were thinking about our conversation today, and we realized something: the people who hire us aren't usually the ones who were stuck from the beginning.

They're usually the ones who got 3–4 weeks in and realized they didn't actually know what they were doing.

Here's what that looks like:

---

**"I Gathered the Wrong Documents"**

Person spends Week 1–2 collecting documents they think they need. Week 3, they contact their consulate with a question. Turns out, they need different docs.

They start over. Lost 2 weeks. Lost motivation. Now annoyed.

Could've been avoided: consulate-specific checklist from day one.

---

**"My Bank Statements Don't Show What I Thought They Showed"**

Person gets 12 months of bank statements. Sits down to organize them. Realizes their monthly deposits look inconsistent (some months €2,500, some €1,800, etc.). Gets nervous. Emails us: "Will this get rejected?"

Answer: Probably not, IF there's a letter from their income source explaining the variation. But they don't have that letter. Now they're scrambling to get it. Adds 2 weeks.

Could've been avoided: knowing upfront what the income source needs to provide in writing.

---

**"My Consulate Wants Documents I've Never Heard Of"**

Person follows the generic Spanish government visa checklist. Submits. Gets email from consulate: "You're missing X and Y."

X and Y aren't on the government website. They're unofficial extras that this particular consulate requires.

Person has to gather new docs. Delays the whole timeline. 4 weeks lost.

Could've been avoided: knowing the consulate's actual requirements, not just the official ones.

---

**"My Translator Delivered the Wrong Format"**

Person hires a translator to translate 5 documents. Translator does competent work. Person submits.

Consulate replies: "Your translations need to be formatted differently." (This is specific to certain consulates.)

Person has to retranslate. Costs another €200. Delays application. 2 weeks lost.

Could've been avoided: knowing the consulate's translation standards before hiring a translator.

---

**The Pattern**

None of these people needed full outsourcing. They didn't need us to hold their hand.

They needed us 3 weeks in when they realized they didn't know something important.

By that point, the mistake was already made.

**Your Real Choice**

You can DIY, and you'll probably be fine. You might hit one of these snags. You might not.

Or you can pay us upfront to avoid the snags and the stress.

**The In-Between Option**

Honestly, we'd rather you work with us than not. But if cost is the issue, know this: you can DIY 80% of this, then bring us in for a document review before you submit.

We can audit your file for €[X] and flag anything that looks like it'll get rejected. That's less expensive than our full service, and it's way less risky than submitting blind.

Not every firm does that. We do, because we think everyone should have access to expertise when it matters.

**Primary CTA:**  
Ready to move forward? [Book another call](#) and let's talk about what makes sense for your situation.

**Secondary CTA:**  
Want to DIY but want a safety check? Reply and we'll tell you the cost to audit your file before you submit.

**Exit Condition:**  
User books another call → upgrade to Branch A if they sign up; stay in Branch B if they don't.  
User replies asking about file audit → sales team provides quote.  
No engagement after Email 5 → move to monthly nurture loop.

---

## Email 5 — Day 30 (Both Branches)
**Goal:** Check-in, confirm engagement, celebrate progress, transition to long-term relationship.

**Subject Line:**  
Next Steps — What Happens Now (You're Doing Great)  
*A/B Alternative:* 30-Day Check-In: How Are You Feeling?

**Preview Text:**  
You're 4 weeks in. Here's what's next.

**Body Copy:**

Hi [First Name],

It's been 30 days since we talked. You're a month into this process. Time for a check-in.

**[If Branch A: Where You Should Be**

You should have:
- Ordered your police certificate (or have it)
- Bank statements in-hand or incoming
- Proof of income gathered or being verified
- Other docs started

You've uploaded a few things to the portal. We've reviewed them. You know what's next.

This is good progress. You're on track.

**What Happens Next**

Week 5–8: You'll gather remaining docs. We'll review as they come in. Goal: by end of Week 8, you have everything and we do a final review before submission.

Week 9: You submit.

Weeks 10–16: You wait and interview.

And we'll be checking in regularly to make sure you're on track.

**How You're Feeling**

You should feel: "I know what's happening. I know what's next. I'm organized."

If you feel: "I'm lost" or "I don't know what I'm doing," reply right now. That's what we're here for.

**How We're Feeling**

Confident. You're gathering documents in the right order. Nothing has come back with red flags. Your consulate is reasonable. This is going to work.

**What to Do This Week**

1. Check your portal for any feedback we left on documents
2. Gather the next batch of docs on your list
3. Reply to this email with one thing: Which doc are you getting this week?

**What to Do This Month**

Keep the momentum. Don't let this sit for 2 weeks. One document per week is a good pace.

---

**[If Branch B: Where You Could Be**

If you decided to DIY, you should be in Week 3–4 of research and document gathering.

If you decided to work with us, you've just started and are in the same place as Branch A clients above.

If you're still deciding, that's okay. But know this: the sooner you decide, the sooner you start gathering. And starting matters. Every week you delay is one week closer to your consulate's deadline (yes, they have seasons; fall gets busier).

**If You're Ready to Move Forward With Us**

[Book a call](#) and we'll get you set up this week.

**If You're DIY-ing**

Keep the checklist handy. You're in Month 1–2 now. The rhythm is: gather, organize, verify you've got everything, then submit in Month 3.

You know where we are if you get stuck.

**One More Thing**

A lot of people at this stage say: "I'm glad I decided to do this. I wasn't sure it was possible, but it feels real now."

If that's you, great. That's the point. This is possible. You're going to be in Spain in 5–6 months.

Hold onto that.

**Primary CTA (Branch A):**  
[Check Your Portal](#) for any feedback on your docs.

**Primary CTA (Branch B):**  
[Ready to Get Help?](#) Book a consultation now and skip the stress.

**Secondary CTA (Both):**  
Reply with what you're gathering this week.

**Exit Condition:**  
[Branch A:] User stays engaged → assign `testimonial_candidate` tag for 4-week follow-up testimonial request.  
[Branch B:] User books call → upgrade to Branch A.  
[Branch B:] No engagement for 14 days → move to monthly nurture, monitor for re-engagement at 8-week and 12-week marks.

---

## Testimonial Collection (Week 4–6, Branch A Only)

After Email 5, tag engaged clients as `testimonial_candidate`. In Week 4–6 post-consultation, send one additional email:

**Subject:** "Can We Share Your Story? (It Only Takes 5 Minutes)"

**Body Gist:** "We're collecting stories from clients who are progressing through the visa process. Would you be willing to answer 5 quick questions about your experience so far? We feature real stories on our site and in our materials. (And it helps future people like you who are researching.)"

**Expected Response Rate:** 40–50%  
**Usage:** Testimonials become case studies, social proof for future campaigns.

---

## CAMPAIGN METRICS & ADJUSTMENT FRAMEWORK

### Open Rate Interpretation

| Rate | Status | Action |
|------|--------|--------|
| 50%+ | Excellent | Keep subject lines similar |
| 40–49% | Good | Monitor for decline |
| 30–39% | Declining | Test new subject lines, check sending time |
| <30% | Poor | Review list quality, consider re-engagement campaign |

### Click Rate Interpretation

| Rate | Status | Action |
|------|--------|--------|
| 18%+ | Excellent | CTA is resonating |
| 12–17% | Good | Content is engaging |
| 8–11% | Below target | Strengthen CTAs, move them higher in email |
| <8% | Poor | Rethink value proposition, test new CTAs |

### Unsubscribe Rate Interpretation

| Rate | Status | Action |
|------|--------|--------|
| <0.5% | Excellent | Keep cadence and content |
| 0.5–1% | Acceptable | Monitor, consider spacing emails out |
| >1% | High | Too frequent or not relevant; cut sending frequency |

### Reply Rate Interpretation

| Rate | Status | Action |
|------|--------|--------|
| 5%+ | Excellent | People trust you; capitalize on engagement |
| 3–4% | Good | Relationships building |
| 1–2% | Low | Consider questions or CTAs that encourage reply |
| <1% | Very low | Emails feel one-way; invite input more explicitly |

---

## NOTES FOR IMPLEMENTATION

- **Personalization Tokens:** [First Name], [Consulate], [Visa Type], [Income Amount], [Start Month] — sync from form data
- **Dynamic Content:** Branch logic should trigger automatically based on form submission answers + consultation outcome flag
- **Testing:** Run A/B tests on subject lines starting Week 2 of each sequence
- **Re-engagement:** For non-converters, implement 8-week "checking in" email, then 12-week "here's what's changed" email
- **Testimonial Automation:** Use post-consultation survey to identify strongest candidates for testimonial outreach
- **Unsubscribe Pages:** Allow users to prefer lower frequency instead of unsubscribing entirely

---

## FILE METADATA

- **Version:** 1.0 (April 2026)
- **Brand:** My Spanish Visa (myspanishvisa.com)
- **Written For:** English-speaking expat audience (UK, US, Canada, Australia, Ireland, South Africa)
- **Total Emails:** 18 (3 sequences: 7 + 6 + 5 + testimonial collection)
- **Total Estimated Copy:** ~8,500 words
- **Expected Campaign Duration:** 75 days (full completion of all three sequences)
- **Next Review:** After 100 test cycles (monitor KPIs and adjust open rates, CTA placement, send times)

