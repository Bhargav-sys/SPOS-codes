code = """
    START 100 
    MACRO
    INCR &X,&Y,&REG=AREG
    MOVER &REG,&X
    ADD &REG,&Y
    MOVEM &REG,&X
    MEND
    MACRO
    DECR &A,&B,&REG=BREG
    MOVER &REG,&A
    SUB &REG,&B
    MOVEM &REG,&A
    MEND
    READ N1
    READ N2
    INCR N1,N2,REG=CREG
    DECR N1,N2
    STOP
    N1 DS 1
    N2 DS 1
    END
"""

split_code = code.split()
print("**************************************************************")
print(split_code)
macro_keyword = "MACRO"

MDT = []
MNT = []
ALA = {}
mntc = 0

i = 0
while i < len(split_code):
    if split_code[i] == macro_keyword:
        macro_name = split_code[i + 1]
        MNT.append(macro_name)
        mntc += 1

        parameters = split_code[i + 2].split(",")
        ala_entry = {}
        for param in parameters:
            if "=" in param:
                param_name, default_value = param.split("=")
                ala_entry[param_name.replace("&", "")] = default_value
            else:
                ala_entry[param.replace("&", "")] = None
        ALA[mntc] = ala_entry

        i += 3
        macro_body = []
        while split_code[i] != "MEND":
            macro_body.append(split_code[i])
            i += 1
        MDT.append((macro_name, macro_body))
    i += 1

print("Macro Definition Table (MDT):")
print(MDT)
print("\nMacro Name Table (MNT):")
print(MNT)
print("\nArgument List Array (ALA) with Default Values:")
print(ALA)

params_used = {}
for idx in range(len(MNT)):
    for r, token in enumerate(split_code):
        if token == MNT[idx]:
            called_params = split_code[r + 1].split(",")
            param_map = ALA[idx + 1].copy()
            for key, value in zip(param_map.keys(), called_params):
                param_map[key] = value
            params_used[MNT[idx]] = param_map

print("\nMacro Parameters in Calls with Defaults Applied:")
print(params_used)

expanded_code = []
for macro_name, macro_body in MDT:
    if macro_name in params_used:
        param_map = params_used[macro_name]
        for token in macro_body:
            for key, value in param_map.items():
                if value is None:
                    value = f"&{key}"
                token = token.replace(f"&{key}", value)
            expanded_code.append(token)
    expanded_code.append("MEND")

print("\nExpanded Code After Parameter Replacement with Defaults:")
print(expanded_code)
