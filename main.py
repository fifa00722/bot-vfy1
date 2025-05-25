import nextcord
from nextcord.ext import commands, tasks
from nextcord import Interaction
from datetime import datetime
import os

TOKEN = ''
Button_name = 'Verify'
Button_emoji = '✅'
member_role_id = 1175732281466437713
logvfy = 1208854185877966878
serverId = 1167330582309646426
ownerIds = [881901702767313017]
imgsetup = 'https://cdn.discordapp.com/attachments/1101085615543566367/1236520231359479878/Untitled_design-removebg-preview_1.png'
# imgthumbnail = 'https://cdn.discordapp.com/attachments/1101085615543566367/1236520231359479878/Untitled_design-removebg-preview_1.png'

intents = nextcord.Intents.default()
intents.members = True


bot = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=intents,
    strip_after_prefix=True,
    case_insensitive=True
)

class vfy(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label=Button_name, style=nextcord.ButtonStyle.green, emoji=Button_emoji, custom_id="vfy", row=1)
    async def vfybotinput(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member_role = interaction.guild.get_role(member_role_id)
        
        if member_role:
            await interaction.user.add_roles(member_role)
            await interaction.response.send_message(
                embed=nextcord.Embed(
                    title="คุณได้รับยศเรียบร้อยแล้ว",
                    description="```หากไม่ได้ยศโปรดติดต่อผู้พัฒนาบอท```",
                    color=0xD1EAF5,
                    timestamp=datetime.now()
                ),
                ephemeral=True
            )
            embed = nextcord.Embed(
                description=f"> ``✅`` รับยศสำเร็จ: <@{interaction.user.id}>\n> ``🔎`` | ยศที่ได้รับ : {member_role.mention}",
                color=nextcord.Color.red(),
                timestamp=datetime.now()
            )
            embed.set_author(name="VERIFICATION SUCCESSFUL !!", icon_url=interaction.user.avatar.url)
            await bot.get_channel(logvfy).send(embed=embed)
        else:
            await interaction.response.send_message(
                embed=nextcord.Embed(
                    title="เกิดข้อผิดพลาด",
                    description="ไม่พบยศที่กำหนด โปรดติดต่อผู้พัฒนาบอท",
                    color=nextcord.Color.red()
                ),
                ephemeral=True
            )



@bot.event
async def on_ready():
    bot.add_view(vfy())  
    os.system("cls" if os.name == "nt" else "clear")
    os.system(f'title LOGIN : {bot.user}')
    print(f"LOGINBOT : {bot.user}")


@bot.slash_command(
    name='vfy',
    description='เซ็ทอัพบอทรับยศ',
    guild_ids=[serverId]
)
async def setupbottellme(interaction: Interaction):
    if interaction.user.id not in ownerIds:
        return await interaction.response.send_message(content='[No Permission]', ephemeral=True)
    embed = nextcord.Embed()
    embed.title = "``✨`` ``:`` BOT VERIFY"
    embed.description = "> 📖 กดปุ่มด้านล่างเพื่อยืนยันตัวตน"
    embed.color = nextcord.Color.green()
    embed.set_image(url=imgsetup)
    # embed.set_thumbnail(url=imgthumbnail) ใส่รูปภาพ Thumbnail
    await interaction.channel.send(embed=embed, view=vfy())
    await interaction.response.send_message(content='[SETUP SUCCESS]', ephemeral=True)


bot.run(TOKEN)
