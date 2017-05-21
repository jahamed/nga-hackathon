from gensim.summarization import summarize, keywords

# text = '''
# Former FBI Director James Comey will testify before the Senate Intelligence Committee in public sometime after Memorial Day.\n\n                                    The committee's chairman, Sen. Richard Burr, and the ranking Democrat, Sen. Mark Warner, announced Friday that Comey will testify in an open setting before the committee. The date of the hearing has not yet been set.\n\n                                    Burr says the committee wants to hear from Comey on his role in the development of the U.S. intelligence agencies' assessment that Russia interfered in last year's election.\n\n                                    He says he hopes Comey's testimony will answer some of the questions that have arisen since Comey was suddenly dismissed last week by President Donald Trump.\n\n                                    This news after reports Friday in the New York Times and the Washington Post about the fallout from Trump's firing of Comey, as well as the inquiry into Russia's role in the 2016 election and possible collusion with the Trump campaign.\n\n                                    The Times reported Friday that Trump told the Russians that recently fired FBI Director James Comey was a \"nut job\" whose ouster relieved \"great pressure\" on him. The Washington Post reported that a senior Trump administration official is now a \"person of interest\" in the Russia probe.\n\n                                    Maryland Rep. Elijah Cummings called Trump's reported comment about Comey \"astonishing and extremely troubling.\"\n\n                                    Cummings said the committee's GOP chairman, Utah Rep. Jason Chaffetz, \"should ... have his subpoena pen ready\" to obtain any White House documents related to Trump's meeting with the Russian foreign minister and ambassador.\n\n                                    Chaffetz has scheduled a hearing on Comey's firing next Wednesday, although it's not clear if Comey will testify.\n\n                                    Meanwhile, Senate Judiciary Committee Chairman Chuck Grassley and Ranking Member Dianne Feinstein today released a statement after Comey declined to testify before their committee that reads in part:\n\n                                    “We’re extremely disappointed in James Comey’s decision not to testify voluntarily before the Judiciary Committee. There is no reason he can’t testify before both the Intelligence and Judiciary Committees, particularly given that the Judiciary Committee is the FBI’s primary oversight committee with broad jurisdiction over federal law enforcement, FISA and the nomination of the next FBI director....He should reconsider his decision.”\n\n                                    Former FBI Director Robert Mueller was named Special Counsel for the Russia investigation on Wednesday.
# '''

text = '''
At a news conference Thursday, Trump angrily denied that he had asked Comey to end the investigation, which is now in the hands of new special counsel Robert Mueller. The President blasted the probe into Russia's involvement in the 2016 election and possible collusion with his campaign as a "witch hunt." 
Comey's view of Trump's intent in their conversations is nuanced, sources say. He initially believed that he could school the new President and White House in what was appropriate during their communications. 
But after his firing, the question of Trump's intent could become more problematic, one source said. Trump told NBC's Lester Holt in an interview that he was thinking "of the Russia thing" when he dismissed Comey.
Sources say Comey had reached no conclusion about the President's intent before he was fired. But Comey did immediately recognize that the new President was not following normal protocols during their interactions.
As The New York Times has reported, after numerous encounters with the administration, Comey felt he had to set the parameters of appropriate protocol very clearly. After the President asked Comey to let it be known publicly he was not under investigation, Comey told the President that if he wanted to know details about the bureau's work he should ask the White House counsel to communicate with the the Justice Department, according to the Times.
According to one source with knowledge, Comey's relationship with Trump was uncomfortable from the start. The director had some hope that, over time, he could effectively point out the appropriate procedures and guidelines to both Trump and the White House staff about how the process of communications normally works. It didn't turn out that way.
One Comey memo reportedly claims that Trump asked the FBI director to "let this go"-- referring to the FBI investigation into Gen. Michael Flynn's contacts with the Russians -- although the President himself has flatly denied that he ever did that.
While it is unknown whether the President has either tapes or notes of his conversations with Comey, the FBI director kept meticulous memos and shared them with his team contemporaneously.
Benjamin Wittes, editor in chief of the Lawfare blog and a Comey friend, writes that Comey called his interactions with Trump "training" in order to "re-establish" appropriate boundaries. In his conversations, Wittes writes, "Comey never specifically said this was about the Russia matter" but he assumed that it was. Comey saw his job, Wittes writes, as an effort to "protect the rest of the bureau from improper contacts and interferences from a group of people he did not regard as honorable."
Wittes told The New York Times that the now-infamous hug from the President -- from which Comey tried to hide behind a blue curtain -- left the director "disgusted." Wittes writes "he regarded the episode as a physical attempt to show closeness and warmth in a fashion calculated to compromise him before Democrats who already mistrusted him."
The dinner with the President, which Wittes describes as "the loyalty dinner," took place five days after that hug.
'''

summary = summarize(text)
# print(summary)

# summary = summarize(text, split=True)
# print(summary)

summary = summarize(text, ratio=0.2)
# print(summary)

# summary = summarize(text, word_count=200)
# print(summary)

print(keywords(summary, ratio=0.2))