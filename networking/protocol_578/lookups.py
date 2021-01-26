from enum import Enum

from . import packets


handshake_packet_lookup = {
    0x00: packets.Handshake,
    0xfe: packets.LegacyServerListPing,
}

status_packet_lookup = {
    0x00: packets.Request,
    0x01: packets.Ping,
}

login_packet_lookup = {
    0x00: packets.LoginStart,
    0x01: packets.EncryptionResponse,
    0x02: packets.LoginPluginResponse,
}

play_packet_lookup = {
    0x00: packets.TeleportConfirm,
    0x01: packets.QueryBlockNbt,
    # 0x02: packets.SetDifficulty,
    0x03: packets.ChatMessageServerbound,
    0x04: packets.ClientStatus,
    0x05: packets.ClientSettings,
    0x06: packets.TabCompleteServerbound,
    0x07: packets.WindowConfirmationServerbound,
    0x08: packets.ClickWindowButton,
    0x09: packets.ClickWindow,
    0x0a: packets.CloseWindowServerbound,
    0x0b: packets.PluginMessageServerbound,
    0x0c: packets.EditBook,
    0x0d: packets.EntityNbtRequest,
    0x0e: packets.InteractEntity,
    0x0f: packets.KeepAliveServerbound,
    # 0x10: packets.LockDifficulty,
    0x11: packets.PlayerPosition,
    0x12: packets.PlayerPositionAndRotationServerbound,
    0x13: packets.PlayerRotation,
    0x14: packets.PlayerMovement,
    0x15: packets.VehicleMoveServerbound,
    0x16: packets.SteerBoat,
    0x17: packets.PickItem,
    0x18: packets.CraftRecipeRequest,
    0x19: packets.PlayerAbilitiesServerbound,
    0x1a: packets.PlayerDigging,
    0x1b: packets.EntityAction,
    0x1c: packets.SteerVehicle,
    0x1d: packets.RecipeBookData,
    0x1e: packets.NameItem,
    0x1f: packets.ResourcePackStatus,
    0x20: packets.AdvancementTab,
    0x21: packets.SelectTrade,
    0x22: packets.SetBeaconEffect,
    0x23: packets.HeldItemChangeServerbound,
    0x24: packets.UpdateCommandBlock,
    0x25: packets.UpdateCommandBlockMinecart,
    0x26: packets.CreativeInventoryAction,
    0x27: packets.UpdateJigsawBlock,
    0x28: packets.UpdateStructureBlock,
    0x29: packets.UpdateSign,
    0x2a: packets.AnimationServerbound,
    0x2b: packets.Spectate,
    0x2c: packets.PlayerBlockPlacement,
    0x2d: packets.UseItem
}

handshake_packet_enum = Enum("Handshake Serverbound Packets", handshake_packet_lookup)
status_packet_enum = Enum("Status Serverbound Packets", status_packet_lookup)
login_packet_enum = Enum("Login Serverbound Packets", login_packet_lookup)
play_packet_enum = Enum("Play Serverbound Packets", play_packet_lookup)
