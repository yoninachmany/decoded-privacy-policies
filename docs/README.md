# decoded-privacy-policies
> Decoded uses crowdsourcing to analyze and outline the contents of the Terms and Conditions of several popular companies to shed light on what consumers are actually agreeing to.

### The Problem

When buying a product or service, people often agree to ridiculous things online, or even sign away rights they aren’t aware of, because they don’t take the time to read 20 page Terms and Conditions. Generally, T&Cs are much better reading material for lawyers than for the people they are supposed to inform. This project will give them the gist of what they are agreeing to, and hopefully incentivize companies to make their policies more clear to consumers.


## 1. /data (5 total)
**Raw data input (1)**

Terms and Condition policies will be gathered from several tech companies, which are easily available in machine-readable form e.g. https://www.facebook.com/legal/terms

**Sample input/output from QC module (2)**

The input will be an entire Terms and Conditions policy, or a significant subsection that we determine.

The output will be shorter than the original Terms and Conditions and will consist of high-level explanations of different sections of the T&C.

A building block for our expected output comes from Genius, the annotation website, which has some annotations for the iTunes Terms of Service document: http://genius.com/1126348.

**Sample input/output from your aggregation module (2)**

Several descriptions for a section of the Terms and Conditions will be compared,
and one will be chosen by majority vote. Then, the results for sections will be concatenated in linear order for the final result.

## 2. /src (4 total)
**Working QC module (2)**

The initial approach for quality control is a simple majority for descriptions of sections of the document. The approach will be tested with a small trial that will identify the benefits and disadvantages of such an approach. Potential paths forward includes adding an additional pass to throw out bad answers that should not be voted on or iterative writing of descriptions.

**Working aggregation (2)**

Given simulated data, the appropriate descriptions for a section of the Terms and Conditions will be chosen and then a final version of the output will be created by appending descriptions in the order of the original sections. In the final version, more work may be required to clean and parse simulated data.

## 3. HIT Prototype (8 total)
* Terms and Conditions documents will need to be chunked before inserting them into HITs to ensure logical breaks. (1)
* Price, redundancy, and potential gold standard data will need to be determined. Crowd will need to speak English and may have comprehension tested. (1)
* Crowd touches data by reading small chunks of Terms and Conditions and translating into high-level explanation, potentially in an iterative manner. (4)
* A small trial will be run to analyze the quality of a simple majority approach and refine the design iteratively. (2)

## 4. Online Resource (3 total)
* Ultimately, the project will result in an online resource that posts crowdsourced summaries alongside original Terms and Conditions policies, to provide consumers with the knowledge of what they’re signing when they agree to use services. (3)

## Q&A for reference
**Who will be the members of your crowd?**

This project will use Mechanical Turk workers to decode what our chosen policies are actually saying by breaking up each policy into segments and having each section summarized by a set of workers, after which another group of workers will determine which of those summaries best encapsulates the content of the section.

**How will you incentivize them to participate?**

We will pay these workers a small sum to participate. There may be a small amount of intrinsic motivation involved as well; a lack of understanding of privacy policies is a problem that affects many internet users, and it’s possible that Turkers will feel that they’re contributing to a worthwhile cause.

**What will they provide, and what sort of skills do they need?**

Turkers will help us determine the main point of a small section of a privacy policy. They will need to speak english and have sufficient analytical and reading comprehension skills to understand what is being stated in the policy. (easier said than done- many policies are primarily written in legal-ese!)

**How will you ensure the quality of the crowd provides? How will you aggregate the results from the crowd?**

We will ultimately create an online resource that posts our crowdsourced summary alongside the original privacy policy, to provide consumers with the knowledge of what they’re signing when they hit “Agree”.

**Describe each of the steps involved in your process. What parts will be done by the crowd, and what parts will be done automatically.**

1. We’ll first have to divide up the privacy policy into different sections, ensuring that the divisions occur at logical breaks in the policy. We will use a machine to do this.
2. We will then survey Mechanical Turk workers and ask them what they think the paragraphs mean. These hits will be run in an iterative process with built in gold-standard questions and multiple summaries written per section. We will encourage Turkers to be as clear and concise as possible in their summaries.
3. Finally, we will add together the summaries for each section and post them onto Mechanical Turk, asking Turkers to mark similar concepts and further summarize the implications for this category. We’ll also build in quality control on this step to ensure that Turkers are writing summaries and voting conscientiously.

**How will you evaluate if your project is successful?**

This project will be successful if we can get Turkers to reliably interpret and summarize the meaning of sections of these privacy policies, and if we are further able to combine these summaries into a useful resource for consumers.

**What potential problems do you foresee when implementing your project?**

We might encounter issues if Turkers are unable to truly understand the legal language that is used in many of these privacy policies, and thus are unable to further explain it clearly to others. This may be problematic for accurately decoding the policies.
Provide a link to your Vimeo video *
