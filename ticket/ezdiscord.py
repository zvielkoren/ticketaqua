import discord

def has_perms(user: discord.User, perm):
    if perm=="create_instant_invite":
        if user.guild_permissions.create_instant_invite:
            return True
        else:
            return False
    if perm=="kick_members":
        if user.guild_permissions.kick_members:
            return True
        else:
            return False
    if perm=="ban_members":
        if user.guild_permissions.ban_members:
            return True
        else:
            return False
    if perm=="administrator":
        if user.guild_permissions.administrator:
            return True
        else:
            return False
    if perm=="manage_channels":
        if user.guild_permissions.manage_channels:
            return True
        else:
            return False
    if perm=="manage_guild":
        if user.guild_permissions.manage_guild:
            return True
        else:
            return False
    if perm=="add_reactions":
        if user.guild_permissions.add_reactions:
            return True
        else:
            return False
    if perm=="view_audit_log":
        if user.guild_permissions.view_audit_log:
            return True
        else:
            return False
    if perm=="priority_speaker":
        if user.guild_permissions.priority_speaker:
            return True
        else:
            return False
    if perm == "stream":
        if user.guild_permissions.stream:
            return True
        else:
            return False
    if perm == "read_messages":
        if user.guild_permissions.read_messages:
            return True
        else:
            return False
    if perm=="view_channel":
        if user.guild_permissions.view_channel:
            return True
        else:
            return False
    if perm=="send_messages":
        if user.guild_permissions.send_messages:
            return True
        else:
            return False
    if perm=="send_tts_messages":
        if user.guild_permissions.send_tts_messages:
            return True
        else:
            return False
    if perm=="manage_messages":
        if user.guild_permissions.manage_messages:
            return True
        else:
            return False
    if perm=="embed_links":
        if user.guild_permissions.embed_links:
            return True
        else:
            return False
    if perm=="attach_files":
        if user.guild_permissions.attach_files:
            return True
        else:
            return False
    if perm=="read_message_history":
        if user.guild_permissions.read_message_history:
            return True
        else:
            return False
    if perm=="mention_everyone":
        if user.guild_permissions.mention_everyone:
            return True
        else:
            return False
    if perm=="external_emojis":
        if user.guild_permissions.external_emojis:
            return True
        else:
            return False
    if perm=="use_external_emojis":
        if user.guild_permissions.use_external_emojis:
            return True
        else:
            return False
    if perm=="view_guild_insights":
        if user.guild_permissions.view_guild_insights:
            return True
        else:
            return False
    if perm=="connect":
        if user.guild_permissions.connect:
            return True
        else:
            return False
    if perm=="speak":
        if user.guild_permissions.speak:
            return True
        else:
            return False
    if perm=="mute_members":
        if user.guild_permissions.mute_members:
            return True
        else:
            return False
    if perm=="deafen_members":
        if user.guild_permissions.deafen_members:
            return True
        else:
            return False
    if perm=="move_members":
        if user.guild_permissions.move_members:
            return True
        else:
            return False
    if perm=="use_voice_activation":
        if user.guild_permissions.use_voice_activation:
            return True
        else:
            return False
    if perm=="change_nickname":
        if user.guild_permissions.change_nickname:
            return True
        else:
            return False
    if perm=="manage_nicknames":
        if user.guild_permissions.manage_nicknames:
            return True
        else:
            return False
    if perm=="manage_permissions" or perm=="manage_roles":
        if user.guild_permissions.manage_permissions:
            return True
        else:
            return False
    if perm=="manage_webhooks":
        if user.guild_permissions.manage_webhooks:
            return True
        else:
            return False
    if perm=="manage_emojis":
        if user.guild_permissions.manage_emojis:
            return True
        else:
            return False
    if perm=="use_slash_commands":
        if user.guild_permissions.use_slash_commands:
            return True
        else:
            return False
    if perm=="request_to_speak":
        if user.guild_permissions.request_to_speak:
            return True
        else:
            return False









