import streamlit

from loader import load_knowledge_logs
from main_interface import start_menu
from streaming_interface import streaming_interface

system_prompt = """Act like a professional marketing strategist and craft a comprehensive marketing strategy for Centerline Athletics.


The strategy should be thorough, covering key areas such as market analysis, target audience, branding, digital marketing, traditional marketing, content strategy, and metrics for success. 


Ensure the strategy is adaptable and tailored to the unique needs of pickleball apparel.

To provide more context:
Centerline Athletics specializes in clothing for and around the pickleball athlete. This athlete-centric approach means every seam, stitch, and fabric choice is made with your performance, comfort, and style in mind. Their design process involves rigorous testing and feedback loops with real athletes to ensure that each piece not only meets but exceeds the demands of high-performance play. From the breathable, moisture-wicking fabrics to the ergonomic fits that enhance movement and flexibility, every detail is crafted to help the athlete find their center and perform at their best. Centerline was built from the ground up, with the athlete in mind. After numerous iterations, alterations, and rounds of feedback, we feel like we have really built a solution for high performance on and off the court. Centerline’s mission is to empower athletes in their pursuit of balance, health, and excellence through meticulously designed performance apparel. Centerline Athletics isn't just a brand; it's a beacon for those who live at the confluence of an active lifestyle and a desire for continuous improvement. Centerline believes that Apparel is more than fabric, seems, hems, and color. It's about the technology and design that goes into each piece, so that it performs up to the same level you aim for yourself. You need your apparel to work with you, not against you. This is why we have teamed up with designers and athletes alike to bring you the very best of on-court performance.  Centerline has developed the groundbreaking GripTek™ technology. Designed to revolutionize your game, GripTek™ is a cutting-edge fabric enhancement that provides unparalleled grip and control in performance wear. Whether you're reaching for a difficult shot in Pickleball or pushing your limits in any other sport, GripTek™ ensures that your clothing works as hard as you do, optimizing your performance and giving you the edge you need to succeed.Our offerings are ultra-breathable fabrics, designed to keep you cool and comfortable, allowing you to stay focused on dominating the game, not the heat. We are known for having a deep understanding that at the core of every athlete, there's a relentless pursuit of balance—finding that perfect harmony between pushing limits and embracing the joy of the game. Their ethos is built on authenticity, driven by the hands-on experience of genuine Pickleball players and active lifestyle enthusiasts who know firsthand what it means to strive for excellence without losing sight of what truly matters.

Our products include mens apparel, womens apparel, womens tops, accessories, airlite, apres play apparel, mens bottoms, mens tops, womens bottoms, at price points ranging from $30.00 to $89.00. 

Here are some of Centerline’s Products and corresponding prices.

Men’s Apparel:
	•	AirLite Men’s Tee: $68
	•	AirLite Men’s Long Sleeve: $72
	•	AirLite 7” Unlined Short: $68
	•	Layering Hoodie Men’s: $75
	•	Apres Men’s Jogger: $85
	•	Apres Unisex Crew Sweatshirt: $85
	•	Apres Unisex Hooded Sweatshirt: $89
	•	Centerline Performance Cap: $30

Women’s Apparel:
	•	AirLite Women’s Tee: $68
	•	AirLite Women’s Long Sleeve: $68
	•	AirLite Women’s Tank: $54
	•	AirLite Skort: $78
	•	Layering Hoodie Women’s: $75
	•	Rise ’n Rally 7/8 Legging: $68
	•	Apres Women’s Jogger: $85
	•	Apres Unisex Crew Sweatshirt: $85
	•	Apres Unisex Hooded Sweatshirt: $89
	•	Centerline Performance Cap: $30

Centerline Athletics primarily operates as an e-commerce business, offering performance apparel through their official website. While they have established partnerships with various organizations, such as DUPR and Civile Apparel, customers are encouraged to purchase directly from their online platform to ensure access to their full product range.

We aim to serve athletes and active individuals who value high-performance, minimalist, and durable apparel. Our business operates nationally via e-commerce, and here’s a detailed breakdown of their target audience:


Demographics
	•	Age Group: 18–45 years old, though the focus may extend to older active individuals who prioritize performance wear.
	•	Gender: Both men and women, with product lines designed to cater to both genders equally.
	•	Income Level: Middle to upper-middle-income groups who are willing to invest in premium athletic wear.
	•	Geography: Primarily North America, focusing on markets with high engagement in fitness, recreational sports, and active lifestyles.

Psychographics
	•	Lifestyle: Active individuals who participate in fitness, sports, or outdoor activities regularly.
	•	Values:
	•	Quality and durability in apparel.
	•	Minimalist designs that combine aesthetics with function.
	•	Sustainable or ethically produced products (if applicable to their branding).
	•	Behavior:
	•	Preference for e-commerce and convenience in shopping.
	•	Loyalty to brands that offer consistent quality and style.

Target Activities
	•	Athletes and Enthusiasts:
	•	Pickleball players (notable given their partnership with DUPR, a pickleball ratings platform).
	•	Recreational and professional athletes engaged in fitness, running, and training.
	•	Active Everyday Wearers:
	•	Individuals seeking comfortable and functional activewear for both athletic and casual use.

Brand Positioning
Centerline Athletics likely positions itself as a premium, niche brand catering to athletes and activewear enthusiasts who prefer quality over mass-market options. By focusing on partnerships and a strong e-commerce presence, they appeal to a digitally-savvy audience.
This information reflects their branding and product strategy as visible from their website and partnerships.


This detailed information will help in tailoring the marketing strategy to our specific needs and market position.

First, conduct an in-depth market analysis to understand the current landscape, including competitors, market trends, and potential opportunities. Use data and insights specific to pickleball apparel to identify gaps and areas for growth. Analyze the strengths, weaknesses, opportunities, and threats (SWOT analysis) relevant to Centerline Athletics and outline the key findings.


Next, define the target audience by segmenting the market into distinct groups based on demographics,psychographics, and behavior. Create detailed buyer personas, describing their needs, pain points, and purchasing behaviors. Explain how our products/services can meet these needs and solve their problems.

Develop a strong brand identity that resonates with the target audience. Define the brand's core values, mission, vision, and unique selling proposition (USP).

Design a compelling brand voice and visual identity, including logos, color schemes, and typography, that aligns with Centerline Athletics's ethos and appeals to our target audience.

Formulate a digital marketing strategy encompassing suitable online channels. Outline a detailed plan for search engine optimization (SEO), content marketing, social media marketing, email marketing, website content and pay-per-click (PPC) advertising. Specify the platforms to focus on, and the type of content to produce to engage and convert the target audience.

Include a traditional marketing approach to complement the digital efforts. Describe strategies,  events, sponsorships, and partnerships. Highlight how these methods can enhance brand visibility and reach within [local/national/global] markets.

Create a content strategy that positions Centerline Athletics as a thought leader in pickleball apparel.

Plan a content calendar that includes blogs, emails, case studies, infographics, videos, and podcasts. Each piece of content should address the pain points of the target audience and offer valuable insights and solutions. Specify the frequency of content publication and the channels for distribution.
Finally, establish metrics for success to measure the effectiveness of the marketing strategy. Define key performance indicators (KPIs) such as website traffic, conversion rates, social media engagement, email open rates, and return on investment (ROI). Set specific, measurable, achievable, relevant, and time-bound (SMART) goals for each KPI. Outline a process for regular review and optimization of the strategy based on performance data and feedback.

Take a deep breath and think step-by-step. Avoid using overly aggressive sales tactics that could alienate potential customers. Instead, focus on building genuine relationships and delivering value through every marketing touchpoint.
"""

context = """Centerline Launch
Recommendation
November 11, 2022Situation & Opportunity
Company stakeholders do not believe the current college license business model is 
viable in the medium / long term.
In an eﬀort to reduce dependency on the current model, ownership wants to explore the 
potential for launching Centerline as an active apparel brand that. 
Resonates with a well deﬁned target audience
Has a compelling brand story that drives demand
Has a strong category focus for product launch
Is readily extendable into multiple sports / consumer passions
Project RecapStakeholder discussions with ownership
Interviews with Subject Matter Experts
Chris Youn Apparel Product Development & Sourcing
Christine Serra Apparel Manufacturing
Sanjay Sood Internationally Renown Branding Expert
Kristen Hill Retail Buyer
Gary Ramirez Apparel reseller
Laura Gainor Leading Pickleball Marketing Expert
Zane Navratil Professional Pickleball Player
Various Members Silverado Country Club
Marketplace assessment
An owner mindset
Recommendations Informed by… 
Project RecapTarget Audience
Centerline Brand Story 
Launch Category 
Product Assortment 
Core Recommendations Inform the Prototype DesignTarget Audience
Casual players of multiple sports
Women and men
Centerline Brand Story 
Launch Category 
Product Assortment 
Core Recommendations Target AudienceGreat Brands are Built to Serve a Particular Audience
Focus on audience is critical 
Creates a foundation for authenticity
Gives consumers a reason to connect, and believe
T arget Audience
Target Audience
Mindset
Health conscious, seek balance, stylish (form + function), 
willing to spend on brands that align with their values
Behavioral 
Play multiple sports. Try then buy. “Oh, this is fun, what 
do I need?” = The Centerline Moment
Demographics 
Adults; 25-54; $60K+ Individual, $100K+ HouseholdMen & Women
Original Hypothesis 
Men are underserved and overlooked
SME input 
Women, traditionally, make, or strongly inﬂuence, the purchase
Recommendation
Build assortment for both at launch. Test, learn, decide how to move forward.
T arget AudienceTarget Audience
Casual players of multiple sports
Women and men
Centerline Brand Story 
Founded to help people live a healthy, balanced life…to ﬁnd their center
Launch Category 
Product Assortment 
Core Recommendations Centerline Brand StoryBuilding a Brand that Matters…Matters
Successful brands have a point of view
More than ever, consumers are seeking authenticity and are making purchase decisions that align with their beliefs 
and core values
64% of global consumers ﬁnd brands that actively communicate their purpose more attractive. 62% want 
companies to take a stand on issues they are passionate about, and 52% say they are more attracted to buy 
from certain brands over others if these brands stand for something bigger than just the products and 
services it sells, which aligns with their personal values. (Accenture 2018)
 
US consumers are more likely to have a positive image of (89%), trust in (86%) and be loyal (83%) to brands 
that lead with purpose. Nearly eight-in-10 (79%) consumers surveyed say they feel a deeper personal 
connection to companies with values similar to their own. And 72% say they feel it is more important than 
ever to buy from companies that reﬂect their values. (Cone/Porter Novelli 2019)
Return on BrandBuilding a Brand that Matters…Matters
Purpose-built brands are sticky and drive loyalty, repeat purchases and higher lifetime values
Brands with a purpose set on improving our quality of life outperform the 
stock market by 120%. (Interbrand 2017)
In 2018, Unilever’s Sustainable Living Brands grew 69% faster than the rest of the 
business, compared to 46% in 2017. (Unilever 2019)
According to Kantar’s Purpose Study, purpose-led brands had seen their valuation surge 
by 175% over the past 12 years, versus a growth rate of just 70% for listless brands 
uncertain of their role. (Kantar 2018)
Return on BrandThe Centerline Brand Story
Create an overarching brand that matters and connects with the audience
Centerline was founded to help people live a healthy, balanced life…to ﬁnd their center
A reminder of what matters
Brings people together through shared enthusiasm
For people who have an aﬃnity for the sports they play
Gives back to the sport, or a cause
Return on BrandReturn on Brand How Brand Investment Pays Oﬀ
Price premium over commodity product
Industry leading purchase conversion rates
Provides customers with social currency that, in turn, drives brand referral
Permission to move into adjacent categories
Loyalty, repurchase and higher lifetime customer value
Relatively small investment in brand message development = low breakeven
Return on BrandReturn on Brand Brand Value Chain
Return on Brand
Marketing 
Program
Customer 
Mindset
Product Market 
Performance
Shareholder
Value
Product
Communications
Trade
Other
Awareness
Associations
Attitudes
Attachment
Activity
Price Premiums
Price Elasticities
Cost Savings
Expansion Success
Market Share
Proﬁtability
Stock Price
P/E Ration
Enterprise Value
Market CapitalizationThe Centerline Brand Model = Business Model
Create an authentic, genuine product, designed by authentic, genuine professional players
Partner with known, or up and coming, individuals who
Align with the core values of the Centerline brand
Collaborate with Centerline design team to create purpose built apparel (form + function)
Are established inﬂuencers and have a following to whom they can promote the brand
Active partners, not just a tacit endorsement
Expansion into adjacent sports / interests
Pickleball, tennis, soccer, yoga, the environment, ﬁnding a cure, etc.
Return on BrandGreat Brands are Built One Category at a Time
Focus matters!
More attention for being known for something vs trying to be everything to everyone
Establish a beachhead
Return on BrandTarget Audience
Casual players of multiple sports
Women and men
Centerline Brand Story 
Founded to help people live a healthy, balanced life…to ﬁnd their center
Launch Category 
Pickleball
Product Assortment
Core Recommendations Launch CategoryLaunch the Brand in the Pickleball Category
Explosive growth and attention
Casual players are pouring into the sport…and this is our target
Equipment manufacturers are established, but the apparel category is wide open…wild west
Launch Category4.8M Players
Ages T otal Core Casual
6-17 21.2% 14.2% 23.9%
18 - 34 28.8% 16.8% 33.5%
35 - 54 20.4% 17.0% 21.8%
55 - 64 12.0% 19.2% 9.2%
65+ 17.6% 32.7% 11.6%
3.5M are casual players (1-7 times per year)
Casual grew by 22% from 2021 to 2022
60% of participants are men 
Players are getting younger 38.1 average age
79% of casual players are under 54
Launch CategoryEquipment Apparel
Selkirk ✔ ✔
Civile ✔
Fila ✔
Joola ✔ ✔
Franklin ✔ ✔
PQL ✔
Brand 
Landscape
“Equipment manufacturers are somewhat sorted out and established, e.g. Selkirk and  
Franklin. But the apparel category is wide open, the wild west”
-Laura Gainor, Pickleball Marketing Expert
Launch CategoryAthletic & 
Athleisure 
Environment
Launch CategoryTarget Audience
Casual players of multiple sports
Women and men
Centerline Brand Story 
Founded to help people live a healthy, balanced life…to ﬁnd their center
Launch Category 
Pickleball
Product Assortment 
8 items
Women 2 tops, 1 bottom, 1 “after play”
Men 2 tops, 1 bottom, 1 “after play”
Core Recommendations Product AssortmentProduct Assortment
This will be informed by our pro players but the 
general framework is…
Test assortment for women and men
Design to outﬁts not items, e.g here’s what you 
need to get dressed for a match…
For Playing on-court
For After oﬀ-court
Assortment
8 items for launch (4 each for women and men)
Individual Items
The Player Top: 2 Styles, $60 each (women: tee, tank; men: tee, ¾ 
sleeve tee)
The Player Bottom; $80 (women: skort); $60 (men; short)
After Play: $80 (zip jacket for women; hoodie for men)
Bundled items
Player Pack One 2 tops, 1 bottom $160 (women) / $145 (men)
Player Pack Two 2 tops, 1 bottom, 1 after play item, $225 (women); 
$210 (men)Target Audience
Casual players of multiple sports
Women and men
Centerline Brand Story 
Founded to help people live a healthy, balanced life…to ﬁnd their center
Launch Category 
Pickleball
Product Assortment 
8 items
Women 2 tops, 1 bottom, 1 “after play”
Men 2 tops, 1 bottom, 1 “after play”
Core Recommendations Additional Discussion1 ✔ Deﬁne
Concise articulation of business situation 
and opportunity.
2 ✔ Decide
Recommendation outlining viability of 
Brand investment as an accelerant to 
revenue growth projections.
3 Design
Go-to-market plan for brand development, 
marketing distribution, and spend. Will now 
include product design, manufacturing, 
distribution and associated costs.
4 Deploy
Growth Catalysts partners will act as 
Centerline’s Activation Network.
Next ActionsApproach
1 ✔ Deﬁne
Concise articulation of business situation and 
opportunity.
2 ✔ Decide
Recommendation outlining viability of 
Brand investment as an accelerant to 
revenue growth projections.
3 Design
Go-to-market plan for brand development, 
marketing distribution, and spend. Will now 
include product design, manufacturing, distribution 
and associated costs.
4 Deploy
Growth Catalysts network partners 
activate the plan as Centerline’s agency.
Next ActionsNext Actions
A  Begin moving forward…build launch prototype  (Design Phase)
Develop Brand Guidelines
Interview and negotiate with players to help design merchandise & represent Centerline
Design, source manufacturer, produce product
Determine sales and marketing distribution channels
Up for sale
Assess results and make go / no go decision
B  Or, ﬁrst, conduct additional research to validate, and reﬁne, initial recommendations 
Ethnographic in-ﬁeld study of Target Audience
Additional interviews with key stakeholders (pros, tour organizers, club / pro shop owners)
Next ActionsFor Reference / Bibliography
Sanjay Sood Marketing, Interview Professor of Marketing UCLA 
Zane Navratil Interview Interview Pickleball Professional and Coach 
Pickleball Central Industry Website for everything Pickleball https://pickleballcentral.com
Laura Gainor Marketing Newsletter Industry Marketing specialist and industry news https://www.linkedin.com/newsletters/pickleball-marketing-news-6987526119562342400/
The Dink Industry News and stories portal https://www.thedinkpickleball.com
Pickler Industry News and stories portal https://thepickler.com
Chris Youn Industry, Interview
Former product development specialist for Abercrombie, Gap, Old 
Navy.
https://docs.google.com/document/d/15WqzDzABmSFf-IFBi5oJpOsIsGf27MPlGS6_SBizOis/edit?usp=sharing
Kristen Hill Industry, Interview
Kristen has almost 20 years of retail experience having worked as a 
buyer and manager at Saks, Bergdorf Goodman, MaxMara, and J. 
Crew.
https://docs.google.com/document/d/1Sw1LPiYZOqKEhgzDxVkTvUxb4HbROvM_EkjvyOZDMBc/edit?usp=sharing
Christine Serra Industry, Interview
Former apparel manufacturing manager Nordstrom 
Civile Apparel Apparel and Equipment Pickleball brand of apparel https://www.civileapparel.com
Kitch Pickleball Apparel and Equipment Pickleball brand of apparel https://kitchpickleball.com
Pickleball Pocket Apparel and Equipment Specialized brand of vests. Also a line of jewelry. https://www.pickleballpocket.com
Selkirk Apparel and Equipment Pickleball-first brand https://www.selkirk.com/
Franklin Apparel and Equipment Apparel and equipment brand https://franklinsports.com/sports/pickleball/apparel
PQL Apparel and Equipment Lux brand of apparel https://pqlclub.com/
Joola Apparel and Equipment Maker's a signature paddle https://joolausa.com/pickleball/?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1PDD6qCcp0tU1OA50mItT8DtA8Pn3Mj4erjdJidt8
wEmWzZ69cST9RoC8VwQAvD_BwE
Original Penguin Apparel and Equipment Old brand https://www.originalpenguin.com/collections/racquet-paddle
Fila Apparel and Equipment Tennis brand https://www.fila.com/pickleball-men
2022 Pickleball Magazine Gear Guide Press The latest gear guide from Pickleball Magazine https://viewer.joomag.com/pickleball-magazine-2022-product-guide/0061678001666617126?short&
Maren Morris Issue Press The latest regular issue of Pickleball Magazine that features Maren 
Morris story. You can see some of the brands in the space in the print 
ads
https://viewer.joomag.com/pickleball-magazine-7-5/0627505001662640175?short&
July/August Issue of Pickleball Magazine
In the centerfold of the July/August issue of Pickleball Magazine, you'll find a compelling story. Check it out here: Pickleball Magazine - Issue 7.4.

Vital Stats (March 2023)
Leadership
Centerline’s leadership is highly experienced in the apparel and retail sectors, with decades of expertise. This includes the acquisition and eventual sale of JanSport, as well as extensive involvement in creating products tailored to enthusiastic audiences. Key team members bring experience from leading companies such as Lululemon, Abercrombie & Fitch, and Apple, positioning Centerline at the forefront of fast-growing sports markets.

The Brand
Centerline was established to promote healthy, balanced living—a reminder of what truly matters. The brand aims to foster community through shared enthusiasm, catering to those passionate about the sports they love and the pursuits they enjoy.

Centerline is built on the principle of authenticity, creating genuine products designed by real players and enthusiasts. To this end, the brand collaborates with influential individuals who:

Align with its core values.
Work with the design team to create functional and purposeful apparel.
Have an established following to promote the brand.
Serve as active partners rather than passive endorsers.
The Category: Active Apparel, Pickleball
Pickleball, the fastest-growing sport in the U.S., has captured the interest of casual players, many of whom are younger and play fewer than eight times per year. This surge presents opportunities for new brands and specialized products.

While equipment brands dominate the market, apparel remains a “wild west” with significant opportunities for innovation. Unlike repurposed tennis or generic athletic clothing, Centerline aims to address the unique needs of pickleball players with purpose-built apparel.

Why Centerline Stands Out
Pickleball enthusiasts are known for their welcoming and inclusive attitudes, making the sport accessible to players of all levels. Recognizing this community spirit, Centerline’s apparel is thoughtfully designed by players, for players, ensuring it combines functionality with style.

As the sport grows, with courts popping up in public spaces, mixed-use destinations, and clubs, Centerline is uniquely positioned to cater to players looking for apparel that complements their love for pickleball—beyond graphics or off-the-shelf gym wear.

Centerline is committed to redefining the category with distinctive, bespoke designs, making it a natural choice for pickleball players passionate about their sport."""

if __name__ == "__main__":
    company_name = "Centerline Atheletics"
    emoji = "🎾"
    company_id = "centerline_athletics"

    start_menu(company_name, company_id)
