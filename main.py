import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import io

plt.rcParams["text.usetex"] = True
params= {'text.latex.preamble' : r'\usepackage{amsmath}'}
plt.rcParams.update(params)

intent = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intent)

@bot.event
async def on_ready():
    print("Connected")

@bot.command(name='watex', help='Bot de test')
async def latex(ctx, *, formule: str):
    latex_code = f'$_{{{formule}}}$'
    plt.text(0.5, 0.5, latex_code, fontsize=50, ha='center', va='center')
    plt.axis('off')
    plt.gcf().set_size_inches(4, 2)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    plt.close()

    await ctx.send(file=discord.File(buf,'Latex.png'))
bot.run("MTIxNjQzNzA5ODc1Njk2NDQ4Mg.GVNVkK.RYF7-M0usGhHmtqiW2r2IqwS61TKKuCLG4Xw2k")
