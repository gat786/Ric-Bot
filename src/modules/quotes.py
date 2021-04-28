"""
This module implements the random quote generator.

Classes: Quotes
Functions: 
    getQuote()
    setup(client)
"""
import random
from discord.ext import commands


class Quotes(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def quotes(self, ctx):
        await ctx.send(getQuote())


def setup(client):
    client.add_cog(Quotes(client))


def getQuote() -> str:
    """Fetches a random quote from the quote list, and returns a string containing quote and author.

    Returns: A string with quote and author.
    """
    QUOTES = {
        "Did you ever stop to think, and forget to start again?": "A. A. Milne",
        "A consultant is someone who saves his client almost enough to pay his fee.": "Arnold H. Glasow",
        "A bigot is simply a sociologist without credentials.": "Dinesh D'Souza",
        "A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.": "Douglas Adams",
        "A fanatic is one who sticks to his guns whether they're loaded or not.": "Franklin P. Jones",
        "A black cat crossing your path signifies that the animal is going somewhere.": "Groucho Marx",
        "I intend to live forever, or die trying.": "Groucho Marx",
        "I refuse to join any club that would have me as a member.": "Groucho Marx",
        "Politics is the art of looking for trouble, finding it everywhere, diagnosing it incorrectly and applying the wrong remedies.": "Groucho Marx",
        "Quote me as saying I was mis-quoted.": "Groucho Marx",
        "Well, Art is Art, isn't it? Still, on the other hand, water is water. And east is east and west is west and if you take cranberries and stew them like applesauce they taste much more like prunes than rhubarb does. Now you tell me what you know.": "Groucho Marx",
        "Why should I care about posterity? What's posterity ever done for me?": "Groucho Marx",
        "A dog is the only thing on earth that loves you more than you love yourself.": "Josh Billings",
        "A good marriage would be between a blind wife and a deaf husband.": "Michel de Montaigne",
        "A drunkard would not give money to sober people. He said they would only eat it": "Samuel Butler",
        "A day without sunshine is like, you know, night.": "Steve Martin",
        "A critic is someone who never actually goes to the battle, yet who afterwards comes out shooting the wounded.": "Tyne Daly",
        "A clever, ugly man every now and then is successful with the ladies, but a handsome fool is irresistible.": "William Makepeace Thackeray",
        "Promise me you'll always remember, You're braver than you believe, and stronger than you seem, and smarter than you think.": "A. A. Milne",
        "A crust eaten in peace is better than a banquet partaken in anxiety.": "Aesop",
        "A creative man is motivated by the desire to achieve, not by the desire to beat others.": "Ayn Rand",
        "A day wasted on others is not wasted on one's self.": "Charles Dickens",
        "A day without laughter is a day wasted.": "Charlie Chaplin",
        "A battle lost or won is easily described, understood, and appreciated": "Frederick Douglass",
        "Leaders should lead as far as they can and then vanish. Their ashes should not choke the fire they have lit.": "H. G. Wells",
        "Our true nationality is mankind.": "H. G. Wells",
        "A barrier is of ideas, not of things.": "Mark Caine",
        "A beautiful thing never gives so much pain as does failing to hear and see it.": "Michelangelo",
        "A goal is a dream with a deadline.": "Napoleon Hill",
        "A fool thinks himself to be wise, but a wise man knows himself to be a fool.": "William Shakespeare",
    }
    QUOTE_QTT = len(QUOTES)
    a = random.randint(0, QUOTE_QTT - 1)
    return list(QUOTES.keys())[a] + " - " + list(QUOTES.values())[a]
