import re
import sys
def load_homoglyphs_dict()->dict:
    #characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.
    #add_more
    dict_of_homoglyphs ={
        "-": ["\\u06d4", "\\u2cba", "\\ufe58", "\\u02d7", "\\u2212", "\\u2796", "\\u2011", "\\u2043", "\\u2012", "\\u2013", "\\u2010"],
        ".": ["\\u0701", "\\u0660", "\\u2024", "\\u06f0", "\\ua60e", "\\ua4f8", "\\u0702", "\\u10a50", "\\uff0e", "\\u1d16d"],
        "0": ["\\u1d476", "\\u0585", "\\u004f", "\\ufbaa", "\\u1d4aa", "\\u06be", "\\u1d70e", "\\u09e6", "\\u0d02", "\\u1d4de", "\\ufee9", "\\u1d630", "\\u06c1", "\\u1ee24", "\\u1d45c", "\\u0a66", "\\u1d7bc", "\\u0c02", "\\u10ff", "\\u1d490", "\\u1d5c8", "\\u0d82", "\\uff4f", "\\u1d744", "\\u0d20", "\\u1d5fc", "\\ufba6", "\\u0c66", "\\u102ab", "\\u1d11", "\\u0665", "\\ufbab", "\\u1d6d0", "\\u1d7b8", "\\u118c8", "\\u104c2", "\\u1d546", "\\uff10", "\\u1d442", "\\u039f", "\\u10292", "\\u1d79e", "\\ufeec", "\\u1d7ce", "\\u1d782", "\\u1d6d4", "\\u06f5", "\\ufbad", "\\ua4f3", "\\ufeeb", "\\u1ee64", "\\u118e0", "\\u10404", "\\u2d54", "\\u1d7ec", "\\ufeea", "\\u3007", "\\u1040", "\\ufba7", "\\u1d77e", "\\u1d428", "\\u0ae6", "\\u118b5", "\\u1d698", "\\u104ea", "\\u0ed0", "\\u05e1", "\\u1d4f8", "\\u0647", "\\u0c82", "\\u0966", "\\u0d66", "\\u1d7e2", "\\u118d7", "\\u1d64a", "\\ufbac", "\\u1d764", "\\u1042c", "\\u1d748", "\\u2134", "\\u1d67e", "\\u0b66", "\\u041e", "\\uab3d", "\\u1ee84", "\\u1d6f0", "\\u1fbf0", "\\u0ce6", "\\u114d0", "\\u1d7d8", "\\u06d5", "\\u1d70a", "\\u1d40e", "\\u0b20", "\\u0e50", "\\u1d52c", "\\u1d594", "\\u1d616", "\\u1d5ae", "\\u03c3", "\\u043e", "\\u12d0", "\\u1d57a", "\\u1d72a", "\\u1d0f", "\\u006f", "\\u03bf", "\\u2c9e", "\\u1d560", "\\u0555", "\\u1d5e2", "\\u10516", "\\u0be6", "\\u07c0", "\\u1d6b6", "\\u1d664", "\\uff2f", "\\u1d512", "\\ufba8", "\\ufba9", "\\u1d7f6", "\\u2c9f", "\\u101d"],
        "1": ["\\u1d55d", "\\u0049", "\\u1d574", "\\u1d43c", "\\u0196", "\\u2d4f", "\\u1ee00", "\\ua4f2", "\\ufe8d", "\\uff4c", "\\u1d661", "\\u2223", "\\u1d6b0", "\\u0406", "\\u2c92", "\\u05c0", "\\u1d7ed", "\\u1d6ea", "\\uff11", "\\u1d610", "\\u05df", "\\u007c", "\\u1d5c5", "\\u1d695", "\\uffe8", "\\u0661", "\\u1d408", "\\u1d540", "\\u05d5", "\\u1d7e3", "\\u1d678", "\\u16f28", "\\u1d5f9", "\\u1d4c1", "\\u1d7f7", "\\u1d724", "\\u1d4f5", "\\u217c", "\\u006c", "\\u1d7cf", "\\u1d5a8", "\\u1d425", "\\u04c0", "\\u10309", "\\u1d5dc", "\\u10320", "\\u1d459", "\\u1e8c7", "\\u23fd", "\\u0399", "\\u01c0", "\\u1d529", "\\u1d470", "\\u1d62d", "\\u07ca", "\\uff29", "\\u2111", "\\u2160", "\\ufe8e", "\\u1ee80", "\\u2113", "\\u1028a", "\\u1d75e", "\\u2110", "\\u1d798", "\\u1fbf1", "\\u1d4d8", "\\u06f1", "\\u1d48d", "\\u1d7d9", "\\u1d644", "\\u0627", "\\u1d591", "\\u16c1"],
        "2": ["\\ua75a", "\\u14bf", "\\u03e8", "\\u1d7ee", "\\ua6ef", "\\u01a7", "\\u1d7da", "\\u1d7e4", "\\u1fbf2", "\\u1d7d0", "\\uff12", "\\ua644", "\\u1d7f8"],
        "3": ["\\u1d7e5", "\\ua76a", "\\u1d7f9", "\\u021c", "\\u1d206", "\\u2ccc", "\\u0417", "\\u04e0", "\\u1d7ef", "\\u01b7", "\\uff13", "\\u1fbf3", "\\u1d7db", "\\u1d7d1", "\\u16f3b", "\\u118ca", "\\ua7ab"],
        "4": ["\\u1d7dc", "\\u1fbf4", "\\u1d7d2", "\\u1d7f0", "\\u118af", "\\u1d7e6", "\\uff14", "\\u13ce", "\\u1d7fa"],
        "5": ["\\u1d7f1", "\\u01bc", "\\u118bb", "\\u1fbf5", "\\u1d7d3", "\\uff15", "\\u1d7fb", "\\u1d7e7", "\\u1d7dd"],
        "6": ["\\u1d7f2", "\\u1d7e8", "\\uff16", "\\u1fbf6", "\\u1d7d4", "\\u118d5", "\\u2cd2", "\\u0431", "\\u13ee", "\\u1d7de", "\\u1d7fc"],
        "7": ["\\u1d7df", "\\u104d2", "\\uff17", "\\u118c6", "\\u1fbf7", "\\u1d7f3", "\\u1d7e9", "\\u1d212", "\\u1d7d5", "\\u1d7fd"],
        "8": ["\\u1d7d6", "\\u1d7fe", "\\u0b03", "\\u1e8cb", "\\u0222", "\\u09ea", "\\u0a6a", "\\u1d7f4", "\\u0223", "\\uff18", "\\u1031a", "\\u1d7e0", "\\u1fbf8", "\\u1d7ea"],
        "9": ["\\u1d7ff", "\\u1fbf9", "\\ua76e", "\\u118ac", "\\u0a67", "\\u1d7d7", "\\u118d6", "\\uff19", "\\u1d7e1", "\\u1d7eb", "\\u09ed", "\\u118cc", "\\u0d6d", "\\u2cca", "\\u0b68", "\\u1d7f5"],
        "A": ["\\u1d6e2", "\\u1d4d0", "\\u1d608", "\\ua4ee", "\\u1d71c", "\\u1d49c", "\\u1d504", "\\uab7a", "\\u1d6a8", "\\u1d5d4", "\\u1d538", "\\u1d63c", "\\u1d56c", "\\u1d670", "\\u0391", "\\u1d434", "\\u16f40", "\\u0410", "\\u15c5", "\\u1d00", "\\u1d400", "\\uff21", "\\u1d756", "\\u102a0", "\\u13aa", "\\u1d5a0", "\\u1d468", "\\u1d790"],
        "B": ["\\u1d539", "\\u1d4d1", "\\u1d671", "\\u0412", "\\u1d5d5", "\\ua7b4", "\\u1d791", "\\u1d56d", "\\u1d757", "\\u10282", "\\u102a1", "\\u0432", "\\u1d6e3", "\\u0392", "\\u1d6a9", "\\u13f4", "\\u15f7", "\\u16d2", "\\u10301", "\\u1d505", "\\u1d469", "\\u1d609", "\\u1d71d", "\\u1d401", "\\u212c", "\\u1d435", "\\u13fc", "\\u1d5a1", "\\u1d63d", "\\ua4d0", "\\uff22", "\\u0299"],
        "C": ["\\u1d672", "\\u1d5a2", "\\u1d60a", "\\u1d436", "\\u118e9", "\\u10415", "\\u13df", "\\u118f2", "\\u212d", "\\uff23", "\\u03f9", "\\u1d4d2", "\\u2ca4", "\\u1d63e", "\\u0421", "\\u1f74c", "\\u216d", "\\u1455", "\\ua4da", "\\u1d46a", "\\u1d49e", "\\u2282", "\\u2102", "\\u2e26", "\\u10302", "\\u1051c", "\\u1d402", "\\u1d56e", "\\u1d5d6", "\\u102a2"],
        "D": ["\\u1d507", "\\u1d63f", "\\u1d49f", "\\u1d673", "\\ua4d3", "\\u1d60b", "\\u2145", "\\u1d46b", "\\u1d5d7", "\\u1d53b", "\\uab70", "\\uff24", "\\u1d5a3", "\\u1d4d3", "\\u1d05", "\\u1d56f", "\\u216e", "\\u13a0", "\\u15ea", "\\u1d437", "\\u15de", "\\u1d403"],
        "E": ["\\u1d46c", "\\u1d6ac", "\\u1d53c", "\\u1d570", "\\u1d5d8", "\\u118a6", "\\u1d404", "\\u1d6e6", "\\u1d508", "\\u22ff", "\\u1d674", "\\u2130", "\\u13ac", "\\ua4f0", "\\u1d794", "\\u2d39", "\\u118ae", "\\u1d640", "\\uff25", "\\uab7c", "\\u1d4d4", "\\u1d438", "\\u1d5a4", "\\u0395", "\\u1d60c", "\\u1d720", "\\u0415", "\\u1d07", "\\u1d75a", "\\u10286"],
        "F": ["\\u1d571", "\\u2131", "\\ua798", "\\u1d405", "\\ua4dd", "\\u118c2", "\\u1d5a5", "\\u1d60d", "\\u118a2", "\\u15b4", "\\u1d675", "\\u1d5d9", "\\u1d46d", "\\u1d641", "\\u10287", "\\u10525", "\\u1d509", "\\uff26", "\\u1d213", "\\u1d7ca", "\\u1d53d", "\\u1d4d5", "\\u1d439", "\\u102a5", "\\u03dc"],
        "G": ["\\u1d4a2", "\\u0262", "\\u13c0", "\\ua4d6", "\\u1d43a", "\\u1d53e", "\\u1d5da", "\\u050c", "\\u1d676", "\\u1d572", "\\u1d60e", "\\u1d4d6", "\\u13f3", "\\u1d642", "\\u1d5a6", "\\u1d46e", "\\uab90", "\\u050d", "\\u1d50a", "\\u1d406", "\\u13fb", "\\uff27"],
        "H": ["\\u210d", "\\u2c8e", "\\uab8b", "\\u1d46f", "\\uff28", "\\u041d", "\\u1d677", "\\u029c", "\\u1d6e8", "\\u1d43b", "\\u1d4d7", "\\u1d5db", "\\u1d573", "\\ua4e7", "\\u1d722", "\\u1d643", "\\u043d", "\\u1d5a7", "\\u0397", "\\u1d796", "\\u157c", "\\u1d407", "\\u102cf", "\\u210b", "\\u210c", "\\u13bb", "\\u1d6ae", "\\u1d60f", "\\u1d75c"],
        "I": ["\\u1d55d", "\\u1d574", "\\u0031", "\\u1d43c", "\\u0196", "\\u2d4f", "\\u1ee00", "\\ua4f2", "\\ufe8d", "\\uff4c", "\\u1d661", "\\u2223", "\\u1d6b0", "\\u0406", "\\u2c92", "\\u05c0", "\\u1d7ed", "\\u1d6ea", "\\uff11", "\\u1d610", "\\u05df", "\\u007c", "\\u1d5c5", "\\u1d695", "\\uffe8", "\\u0661", "\\u1d408", "\\u1d540", "\\u05d5", "\\u1d7e3", "\\u1d678", "\\u16f28", "\\u1d5f9", "\\u1d4c1", "\\u1d7f7", "\\u1d724", "\\u1d4f5", "\\u217c", "\\u006c", "\\u1d7cf", "\\u1d5a8", "\\u1d425", "\\u04c0", "\\u10309", "\\u1d5dc", "\\u10320", "\\u1d459", "\\u1e8c7", "\\u23fd", "\\u0399", "\\u01c0", "\\u1d529", "\\u1d470", "\\u1d62d", "\\u07ca", "\\uff29", "\\u2111", "\\u2160", "\\ufe8e", "\\u1ee80", "\\u2113", "\\u1028a", "\\u1d75e", "\\u2110", "\\u1d798", "\\u1fbf1", "\\u1d4d8", "\\u06f1", "\\u1d48d", "\\u1d7d9", "\\u1d644", "\\u0627", "\\u1d591", "\\u16c1"],
        "J": ["\\u0408", "\\ua7b2", "\\u1d645", "\\u1d50d", "\\u1d5a9", "\\u1d575", "\\u1d5dd", "\\uab7b", "\\u1d409", "\\u1d0a", "\\u148d", "\\uff2a", "\\u1d611", "\\u1d43d", "\\u1d679", "\\ua4d9", "\\u1d4a5", "\\u037f", "\\u1d541", "\\u1d471", "\\u1d4d9", "\\u13ab"],
        "K": ["\\u16d5", "\\u1d646", "\\u1d4a6", "\\u1d5aa", "\\u1d43e", "\\u039a", "\\u1d542", "\\ua4d7", "\\u1d4da", "\\u1d5de", "\\u1d612", "\\u1d6b1", "\\u10518", "\\u1d6eb", "\\u1d576", "\\u041a", "\\u1d75f", "\\uff2b", "\\u13e6", "\\u1d799", "\\u1d50e", "\\u1d67a", "\\u1d472", "\\u1d40a", "\\u1d725", "\\u2c94", "\\u212a"],
        "L": ["\\u2cd1", "\\u1d647", "\\u1d43f", "\\u1d5ab", "\\u1d5df", "\\uabae", "\\u1d613", "\\uff2c", "\\u1d473", "\\u1d50f", "\\u10526", "\\u1d577", "\\u1d67b", "\\u10443", "\\ua4e1", "\\u16f16", "\\u216c", "\\u14aa", "\\u2cd0", "\\u118a3", "\\u1d543", "\\u029f", "\\u1d40b", "\\u118b2", "\\u1d4db", "\\u2112", "\\u13de", "\\u1d22a", "\\u1041b"],
        "M": ["\\u102b0", "\\u1d4dc", "\\u216f", "\\u10311", "\\u15f0", "\\u1d5ac", "\\u16d6", "\\u1d614", "\\u039c", "\\u1d510", "\\u1d761", "\\u1d6b3", "\\u1d727", "\\u1d40c", "\\u1d474", "\\u1d67c", "\\u1d5e0", "\\u13b7", "\\u1d440", "\\u041c", "\\u2133", "\\ua4df", "\\u1d578", "\\uff2d", "\\u1d79b", "\\u03fa", "\\u1d648", "\\u1d6ed", "\\u1d544", "\\u2c98"],
        "N": ["\\u1d441", "\\u1d762", "\\u2c9a", "\\u1d5ad", "\\u1d615", "\\u1d40d", "\\u0274", "\\u1d6b4", "\\u1d579", "\\u1d4a9", "\\u1d649", "\\ua4e0", "\\u1d728", "\\u2115", "\\u10513", "\\u1d5e1", "\\u1d4dd", "\\u1d79c", "\\u1d511", "\\u1d6ee", "\\uff2e", "\\u1d475", "\\u1d67d", "\\u039d"],
        "O": ["\\u1d476", "\\u0585", "\\ufbaa", "\\u1d4aa", "\\u06be", "\\u1d70e", "\\u09e6", "\\u0d02", "\\u1d4de", "\\ufee9", "\\u1d630", "\\u06c1", "\\u1ee24", "\\u1d45c", "\\u0a66", "\\u1d7bc", "\\u0c02", "\\u10ff", "\\u1d490", "\\u1d5c8", "\\u0d82", "\\uff4f", "\\u1d744", "\\u0d20", "\\u1d5fc", "\\ufba6", "\\u0c66", "\\u102ab", "\\u1d11", "\\u0665", "\\ufbab", "\\u1d6d0", "\\u1d7b8", "\\u118c8", "\\u0030", "\\u104c2", "\\u1d546", "\\uff10", "\\u1d442", "\\u039f", "\\u10292", "\\u1d79e", "\\ufeec", "\\u1d7ce", "\\u1d782", "\\u1d6d4", "\\u06f5", "\\ufbad", "\\ua4f3", "\\ufeeb", "\\u1ee64", "\\u118e0", "\\u10404", "\\u2d54", "\\u1d7ec", "\\ufeea", "\\u3007", "\\u1040", "\\ufba7", "\\u1d77e", "\\u1d428", "\\u0ae6", "\\u118b5", "\\u1d698", "\\u104ea", "\\u0ed0", "\\u05e1", "\\u1d4f8", "\\u0647", "\\u0c82", "\\u0966", "\\u0d66", "\\u1d7e2", "\\u118d7", "\\u1d64a", "\\ufbac", "\\u1d764", "\\u1042c", "\\u1d748", "\\u2134", "\\u1d67e", "\\u0b66", "\\u041e", "\\uab3d", "\\u1ee84", "\\u1d6f0", "\\u1fbf0", "\\u0ce6", "\\u114d0", "\\u1d7d8", "\\u06d5", "\\u1d70a", "\\u1d40e", "\\u0b20", "\\u0e50", "\\u1d52c", "\\u1d594", "\\u1d616", "\\u1d5ae", "\\u03c3", "\\u043e", "\\u12d0", "\\u1d57a", "\\u1d72a", "\\u1d0f", "\\u006f", "\\u03bf", "\\u2c9e", "\\u1d560", "\\u0555", "\\u1d5e2", "\\u10516", "\\u0be6", "\\u07c0", "\\u1d6b6", "\\u1d664", "\\uff2f", "\\u1d512", "\\ufba8", "\\ufba9", "\\u1d7f6", "\\u2c9f", "\\u101d"],
        "P": ["\\uabb2", "\\u1d5e3", "\\u1d29", "\\u1d4ab", "\\uff30", "\\u1d64b", "\\u1d5af", "\\u1d513", "\\u0420", "\\u2119", "\\u1d67f", "\\u1d4df", "\\ua4d1", "\\u1d6b8", "\\u03a1", "\\u1d57b", "\\u1d766", "\\u1d7a0", "\\u10295", "\\u1d18", "\\u1d443", "\\u146d", "\\u1d40f", "\\u2ca2", "\\u1d6f2", "\\u1d617", "\\u13e2", "\\u1d72c", "\\u1d477"],
        "Q": ["\\u1d4ac", "\\u1d57c", "\\u2d55", "\\u1d478", "\\u1d444", "\\u1d410", "\\u211a", "\\u1d514", "\\u1d64c", "\\uff31", "\\u1d618", "\\u1d5b0", "\\u1d680", "\\u1d5e4", "\\u1d4e0"],
        "R": ["\\u1d479", "\\u211c", "\\uab71", "\\u1d216", "\\u1d5e5", "\\u1587", "\\u0280", "\\u1d5b1", "\\u1d411", "\\u16b1", "\\u01a6", "\\u13a1", "\\uff32", "\\u211b", "\\uaba2", "\\u1d64d", "\\u13d2", "\\u104b4", "\\u1d57d", "\\u211d", "\\u1d445", "\\u1d681", "\\u16f35", "\\u1d4e1", "\\ua4e3", "\\u1d619"],
        "S": ["\\u054f", "\\uff33", "\\u1d4e2", "\\u1d57e", "\\u1d5b2", "\\u10296", "\\u13da", "\\u1d47a", "\\u1d446", "\\u1d4ae", "\\u1d61a", "\\u1d64e", "\\u10420", "\\u13d5", "\\u1d5e6", "\\ua4e2", "\\u1d516", "\\u1d412", "\\u1d54a", "\\u16f3a", "\\u1d682", "\\u0405"],
        "T": ["\\u1d6d5", "\\u1d683", "\\u1d47b", "\\u1d54b", "\\u27d9", "\\u2ca6", "\\u16f0a", "\\u1d1b", "\\u1d413", "\\u10297", "\\uab72", "\\u1d4e3", "\\u1d7bd", "\\u1d61b", "\\u03c4", "\\u1d6bb", "\\u1d783", "\\u22a4", "\\u0422", "\\u0442", "\\u1f768", "\\u1d5b3", "\\u1d769", "\\u1d6f5", "\\u1d4af", "\\u1d5e7", "\\u1d64f", "\\u03a4", "\\u102b1", "\\u1d517", "\\uff34", "\\u1d7a3", "\\u1d749", "\\u1d447", "\\u1d70f", "\\u13a2", "\\ua4d4", "\\u1d72f", "\\u118bc", "\\u10315", "\\u1d57f"],
        "U": ["\\u1d448", "\\u1d414", "\\u22c3", "\\u222a", "\\u1d5b4", "\\u1d518", "\\u1d580", "\\u1d47c", "\\u1d4b0", "\\u1d650", "\\u144c", "\\u104ce", "\\u1d4e4", "\\u1d5e8", "\\u1d61c", "\\u1d684", "\\u118b8", "\\u16f42", "\\ua4f4", "\\u1d54c", "\\u1200", "\\uff35", "\\u054d"],
        "V": ["\\u1d415", "\\u1d685", "\\u1051d", "\\u2164", "\\u1d581", "\\u13d9", "\\u142f", "\\u0474", "\\ua6df", "\\u2d38", "\\u06f7", "\\uff36", "\\u1d20d", "\\u1d54d", "\\u1d449", "\\u1d61d", "\\u1d4b1", "\\u1d47d", "\\u1d5b5", "\\u118a0", "\\ua4e6", "\\u1d519", "\\u0667", "\\u1d4e5", "\\u1d5e9", "\\u16f08", "\\u1d651"],
        "W": ["\\u1d686", "\\u118e6", "\\u051c", "\\u1d652", "\\u1d47e", "\\u1d4b2", "\\u1d416", "\\u1d4e6", "\\u1d5ea", "\\u118ef", "\\u1d51a", "\\u13d4", "\\u1d5b6", "\\uff37", "\\u1d54e", "\\u1d44a", "\\u1d582", "\\u13b3", "\\ua4ea", "\\u1d61e"],
        "X": ["\\u1d5b7", "\\u2169", "\\u1d7a6", "\\u1d4b3", "\\u10322", "\\u2573", "\\u1d61f", "\\u03a7", "\\u1d6be", "\\u10290", "\\u102b4", "\\u1d54f", "\\u10317", "\\ua4eb", "\\u2cac", "\\u1d47f", "\\u0425", "\\uff38", "\\u1d51b", "\\u1d76c", "\\u1d44b", "\\u118ec", "\\u166d", "\\u1d417", "\\u1d732", "\\u2d5d", "\\u10527", "\\u1d583", "\\u1d653", "\\u1d5eb", "\\u1d687", "\\u1d6f8", "\\ua7b3", "\\u1d4e7", "\\u16b7"],
        "Y": ["\\u1d584", "\\ua4ec", "\\u03a5", "\\u1d4b4", "\\u1d688", "\\u1d480", "\\u102b2", "\\u1d620", "\\u1d550", "\\u1d76a", "\\u1d654", "\\u13bd", "\\u1d5ec", "\\u2ca8", "\\u1d6bc", "\\u13a9", "\\u1d7a4", "\\u1d730", "\\u1d418", "\\u0423", "\\u1d4e8", "\\u118a4", "\\uff39", "\\u04ae", "\\u16f43", "\\u1d51c", "\\u03d2", "\\u1d44c", "\\u1d6f6", "\\u1d5b8"],
        "Z": ["\\u1d44d", "\\u102f5", "\\u1d6e7", "\\u1d689", "\\uff3a", "\\u2124", "\\u0396", "\\u1d655", "\\u1d6ad", "\\u1d621", "\\u1d721", "\\u1d75b", "\\u1d481", "\\u1d585", "\\u1d419", "\\ua4dc", "\\u1d5b9", "\\u1d4e9", "\\u13c3", "\\u1d795", "\\u1d4b5", "\\u1d5ed", "\\u118a9", "\\u118e5", "\\u2128"],
        "a": ["\\uff41", "\\u0251", "\\u03b1", "\\u1d41a", "\\u1d656", "\\u1d770", "\\u1d482", "\\u1d68a", "\\u237a", "\\u1d7aa", "\\u1d4b6", "\\u0430", "\\u1d51e", "\\u1d5ee", "\\u1d622", "\\u1d552", "\\u1d5ba", "\\u1d44e", "\\u1d6fc", "\\u1d6c2", "\\u1d4ea", "\\u1d736", "\\u1d586"],
        "b": ["\\u1d483", "\\u1d41b", "\\u1d4b7", "\\u1d5bb", "\\u15af", "\\u1d587", "\\u1d623", "\\u13cf", "\\u1d4eb", "\\u0184", "\\u1d5ef", "\\u1d553", "\\u042c", "\\u1d51f", "\\u1d44f", "\\uff42", "\\u1d68b", "\\u1d657", "\\u1472"],
        "c": ["\\u1d520", "\\u1d450", "\\u1d5f0", "\\u217d", "\\u1d588", "\\u1d04", "\\u1043d", "\\uabaf", "\\u1d4ec", "\\u1d624", "\\u1d41c", "\\u1d5bc", "\\u1d658", "\\u0441", "\\u1d554", "\\u03f2", "\\u2ca5", "\\u1d68c", "\\u1d484", "\\u1d4b8", "\\uff43"],
        "d": ["\\u1d5f1", "\\u13e7", "\\u1d41d", "\\u1d4b9", "\\u2146", "\\ua4d2", "\\u0501", "\\uff44", "\\u1d589", "\\u1d521", "\\u1d68d", "\\u1d659", "\\u1d5bd", "\\u146f", "\\u1d451", "\\u1d625", "\\u217e", "\\u1d555", "\\u1d485", "\\u1d4ed"],
        "e": ["\\u212f", "\\u1d522", "\\u04bd", "\\uff45", "\\u1d556", "\\u2147", "\\u1d65a", "\\u212e", "\\uab32", "\\u1d486", "\\u1d5f2", "\\u1d452", "\\u1d5be", "\\u1d4ee", "\\u1d58a", "\\u1d626", "\\u1d68e", "\\u0435", "\\u1d41e"],
        "f": ["\\u1d65b", "\\u1d487", "\\u017f", "\\u1d4bb", "\\u1d523", "\\u0584", "\\u1d7cb", "\\u1d5f3", "\\uff46", "\\u1d68f", "\\u1d58b", "\\uab35", "\\u1d4ef", "\\u1e9d", "\\u1d557", "\\u1d5bf", "\\u1d453", "\\u1d41f", "\\u03dd", "\\u1d627", "\\ua799"],
        "g": ["\\u1d58c", "\\u1d420", "\\u210a", "\\u1d5f4", "\\u1d558", "\\u1d65c", "\\u0261", "\\u1d524", "\\u1d690", "\\u018d", "\\u0581", "\\u1d5c0", "\\u1d628", "\\uff47", "\\u1d488", "\\u1d83", "\\u1d4f0", "\\u1d454"],
        "h": ["\\u1d421", "\\u1d4bd", "\\uff48", "\\u1d58d", "\\u1d65d", "\\u1d691", "\\u1d559", "\\u1d5c1", "\\u1d629", "\\u13c2", "\\u0570", "\\u1d5f5", "\\u1d4f1", "\\u210e", "\\u1d489", "\\u1d525", "\\u04bb"],
        "i": ["\\u1d62a", "\\u1fbe", "\\u2148", "\\u1d778", "\\u1d58e", "\\u1d422", "\\u04cf", "\\u037a", "\\uff49", "\\u1d5c2", "\\u1d73e", "\\ua647", "\\u1d5f6", "\\u13a5", "\\u1d65e", "\\u118c3", "\\u0269", "\\u1d4be", "\\u1d6a4", "\\u2373", "\\u1d526", "\\u1d456", "\\u03b9", "\\u1d4f2", "\\u1d6ca", "\\u1d7b2", "\\u1d48a", "\\u1d692", "\\u026a", "\\u1d704", "\\u02db", "\\uab75", "\\u0456", "\\u2170", "\\u2139", "\\u1d55a", "\\u0131"],
        "j": ["\\u1d423", "\\u1d5c3", "\\u1d693", "\\u2149", "\\u1d55b", "\\u03f3", "\\uff4a", "\\u1d48b", "\\u1d457", "\\u1d4bf", "\\u1d65f", "\\u0458", "\\u1d527", "\\u1d62b", "\\u1d5f7", "\\u1d4f3", "\\u1d58f"],
        "k": ["\\uff4b", "\\u1d55c", "\\u1d458", "\\u1d424", "\\u1d660", "\\u1d694", "\\u1d590", "\\u1d5c4", "\\u1d5f8", "\\u1d528", "\\u1d62c", "\\u1d48c", "\\u1d4f4", "\\u1d4c0"],
        "l": ["\\u1d55d", "\\u0049", "\\u1d574", "\\u0031", "\\u1d43c", "\\u0196", "\\u2d4f", "\\u1ee00", "\\ua4f2", "\\ufe8d", "\\uff4c", "\\u1d661", "\\u2223", "\\u1d6b0", "\\u0406", "\\u2c92", "\\u05c0", "\\u1d7ed", "\\u1d6ea", "\\uff11", "\\u1d610", "\\u05df", "\\u007c", "\\u1d5c5", "\\u1d695", "\\uffe8", "\\u0661", "\\u1d408", "\\u1d540", "\\u05d5", "\\u1d7e3", "\\u1d678", "\\u16f28", "\\u1d5f9", "\\u1d4c1", "\\u1d7f7", "\\u1d724", "\\u1d4f5", "\\u217c", "\\u1d7cf", "\\u1d5a8", "\\u1d425", "\\u04c0", "\\u10309", "\\u1d5dc", "\\u10320", "\\u1d459", "\\u1e8c7", "\\u23fd", "\\u0399", "\\u01c0", "\\u1d529", "\\u1d470", "\\u1d62d", "\\u07ca", "\\uff29", "\\u2111", "\\u2160", "\\ufe8e", "\\u1ee80", "\\u2113", "\\u1028a", "\\u1d75e", "\\u2110", "\\u1d798", "\\u1fbf1", "\\u1d4d8", "\\u06f1", "\\u1d48d", "\\u1d7d9", "\\u1d644", "\\u0627", "\\u1d591", "\\u16c1"],
        "m": ["\\uff4d"],
        "n": ["\\u1d52b", "\\u1d593", "\\u1d5c7", "\\u1d45b", "\\uff4e", "\\u1d5fb", "\\u0578", "\\u1d62f", "\\u1d4f7", "\\u1d663", "\\u1d48f", "\\u1d4c3", "\\u1d55f", "\\u1d697", "\\u1d427", "\\u057c"],
        "o": ["\\u1d476", "\\u0585", "\\u004f", "\\ufbaa", "\\u1d4aa", "\\u06be", "\\u1d70e", "\\u09e6", "\\u0d02", "\\u1d4de", "\\ufee9", "\\u1d630", "\\u06c1", "\\u1ee24", "\\u1d45c", "\\u0a66", "\\u1d7bc", "\\u0c02", "\\u10ff", "\\u1d490", "\\u1d5c8", "\\u0d82", "\\uff4f", "\\u1d744", "\\u0d20", "\\u1d5fc", "\\ufba6", "\\u0c66", "\\u102ab", "\\u1d11", "\\u0665", "\\ufbab", "\\u1d6d0", "\\u1d7b8", "\\u118c8", "\\u0030", "\\u104c2", "\\u1d546", "\\uff10", "\\u1d442", "\\u039f", "\\u10292", "\\u1d79e", "\\ufeec", "\\u1d7ce", "\\u1d782", "\\u1d6d4", "\\u06f5", "\\ufbad", "\\ua4f3", "\\ufeeb", "\\u1ee64", "\\u118e0", "\\u10404", "\\u2d54", "\\u1d7ec", "\\ufeea", "\\u3007", "\\u1040", "\\ufba7", "\\u1d77e", "\\u1d428", "\\u0ae6", "\\u118b5", "\\u1d698", "\\u104ea", "\\u0ed0", "\\u05e1", "\\u1d4f8", "\\u0647", "\\u0c82", "\\u0966", "\\u0d66", "\\u1d7e2", "\\u118d7", "\\u1d64a", "\\ufbac", "\\u1d764", "\\u1042c", "\\u1d748", "\\u2134", "\\u1d67e", "\\u0b66", "\\u041e", "\\uab3d", "\\u1ee84", "\\u1d6f0", "\\u1fbf0", "\\u0ce6", "\\u114d0", "\\u1d7d8", "\\u06d5", "\\u1d70a", "\\u1d40e", "\\u0b20", "\\u0e50", "\\u1d52c", "\\u1d594", "\\u1d616", "\\u1d5ae", "\\u03c3", "\\u043e", "\\u12d0", "\\u1d57a", "\\u1d72a", "\\u1d0f", "\\u03bf", "\\u2c9e", "\\u1d560", "\\u0555", "\\u1d5e2", "\\u10516", "\\u0be6", "\\u07c0", "\\u1d6b6", "\\u1d664", "\\uff2f", "\\u1d512", "\\ufba8", "\\ufba9", "\\u1d7f6", "\\u2c9f", "\\u101d"],
        "p": ["\\u1d45d", "\\u1d561", "\\u1d78e", "\\u03f1", "\\u1d7c8", "\\u1d70c", "\\uff50", "\\u2ca3", "\\u1d4c5", "\\u1d7ba", "\\u1d491", "\\u1d595", "\\u1d746", "\\u1d429", "\\u1d71a", "\\u1d665", "\\u1d754", "\\u1d780", "\\u1d52d", "\\u1d699", "\\u03c1", "\\u2374", "\\u1d5c9", "\\u1d6e0", "\\u1d5fd", "\\u0440", "\\u1d631", "\\u1d6d2", "\\u1d4f9"],
        "q": ["\\u051b", "\\uff51", "\\u1d4fa", "\\u1d5ca", "\\u1d52e", "\\u1d562", "\\u1d45e", "\\u1d5fe", "\\u1d666", "\\u1d596", "\\u1d69a", "\\u0563", "\\u1d492", "\\u1d632", "\\u1d42a", "\\u0566", "\\u1d4c6"],
        "r": ["\\u1d597", "\\u1d4fb", "\\u2c85", "\\u1d5cb", "\\u1d45f", "\\uab47", "\\u1d69b", "\\u1d42b", "\\u1d667", "\\u0433", "\\u1d493", "\\u1d4c7", "\\uab48", "\\u1d5ff", "\\uff52", "\\u1d52f", "\\u1d26", "\\u1d563", "\\uab81", "\\u1d633"],
        "s": ["\\u1d69c", "\\ua731", "\\uabaa", "\\u1d600", "\\u01bd", "\\u0455", "\\u1d460", "\\u118c1", "\\u1d564", "\\u1d668", "\\u1d4fc", "\\u1d494", "\\u1d5cc", "\\u1d634", "\\u1d42c", "\\u10448", "\\u1d530", "\\u1d598", "\\uff53", "\\u1d4c8"],
        "t": ["\\u1d495", "\\u1d5cd", "\\u1d599", "\\u1d669", "\\u1d531", "\\u1d4fd", "\\u1d4c9", "\\u1d42d", "\\u1d601", "\\u1d461", "\\u1d69d", "\\u1d565", "\\uff54", "\\u1d635"],
        "u": ["\\u1d462", "\\u104f6", "\\u1d5ce", "\\u1d6d6", "\\u1d1c", "\\uff55", "\\u1d42e", "\\u1d59a", "\\u1d69e", "\\u1d710", "\\u1d602", "\\u1d636", "\\u1d496", "\\u1d532", "\\u1d66a", "\\u118d8", "\\u03c5", "\\u1d7be", "\\u1d4ca", "\\u1d4fe", "\\u1d566", "\\u057d", "\\uab4e", "\\uab52", "\\ua79f", "\\u1d784", "\\u028b", "\\u1d74a"],
        "v": ["\\u1d66b", "\\u1d4ff", "\\u0475", "\\u1d7b6", "\\uff56", "\\u1d497", "\\u1d533", "\\u1d77c", "\\u1d603", "\\u1d69f", "\\u1d42f", "\\u1d20", "\\u1d4cb", "\\u1d59b", "\\u05d8", "\\u22c1", "\\u1d742", "\\u1d6ce", "\\u11706", "\\u03bd", "\\u1d708", "\\u1d463", "\\u2228", "\\u1d637", "\\u1d5cf", "\\uaba9", "\\u118c0", "\\u2174", "\\u1d567"],
        "w": ["\\u1d604", "\\uff57", "\\u1d5d0", "\\u1d498", "\\u1d430", "\\u1170f", "\\u1d638", "\\u1d66c", "\\u1d59c", "\\u1d534", "\\u1d500", "\\uab83", "\\u1d464", "\\u026f", "\\u1170a", "\\u0561", "\\u1d6a0", "\\u1d568", "\\u1d21", "\\u1d4cc", "\\u0461", "\\u1170e", "\\u051d"],
        "x": ["\\u1d431", "\\u1d465", "\\u2a2f", "\\u1d535", "\\u1d5d1", "\\u0445", "\\u157d", "\\u1d639", "\\u1d4cd", "\\u1d499", "\\u2179", "\\u292c", "\\u1d605", "\\u00d7", "\\u166e", "\\u1d6a1", "\\uff58", "\\u1541", "\\u1d569", "\\u292b", "\\u1d59d", "\\u1d501", "\\u1d66d"],
        "y": ["\\uab5a", "\\u1eff", "\\u0443", "\\u028f", "\\u1d606", "\\u213d", "\\u1d772", "\\u04af", "\\u10e7", "\\u1d56a", "\\u1d4ce", "\\u1d6c4", "\\u1d63a", "\\uff59", "\\u1d66e", "\\u1d738", "\\u0263", "\\u1d7ac", "\\u1d502", "\\u1d466", "\\u1d6a2", "\\u03b3", "\\u1d536", "\\u1d8c", "\\u1d49a", "\\u118dc", "\\u1d432", "\\u1d59e", "\\u1d6fe", "\\u1d5d2"],
        "z": ["\\u1d49b", "\\u1d433", "\\u1d59f", "\\u1d63b", "\\u1d56b", "\\u1d607", "\\u1d537", "\\u1d22", "\\u1d4cf", "\\uab93", "\\u1d467", "\\u1d66f", "\\u1d6a3", "\\u118c4", "\\u1d503", "\\u1d5d3", "\\uff5a"]
        }
    return dict_of_homoglyphs

    pass
def load_file(file_name:str):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        return content
def get_non_ascii_list(input_text:str)->list:
    result_list=[]
    for sign in input_text:
        sign_code = ord(sign)
        unicode_of_sign= chr(sign_code).encode('ascii', 'backslashreplace').decode("utf-8")
        if(sign_code>127):
            result_list.append(unicode_of_sign)
    return result_list
def find_homoglyphs(dict_of_homoglyphs:dict, list_of_homogliphs):
    for key in dict_of_homoglyphs:
        for homoglyph in dict_of_homoglyphs[key]:
            if(homoglyph in list_of_homogliphs):
                print("found")
#response:
#index of homoglygh
#original sign
#get_index()
def main():
    args = sys.argv[1:]
    input_data = load_file(str(args[0]))
    #print(get_non_ascii_list(input_data))
    find_homoglyphs(load_homoglyphs_dict(), get_non_ascii_list(input_data))

if __name__ == '__main__':
    main()