# Exp 3 · f(W,X,Y,Z) = Σm(1,3,5,7,8,12,14) with basic gates, NAND only, NOR only

<div class="sub">Manual p. 10 · ICs 7404, 7408, 7411, 7432 (basic); 7400 + 7410 (NAND); 7402 + 7427 (NOR) · all four forms checked over all 16 inputs</div>

[[map:1 Gates & universality > 2 Adders/subtractors > 3 NAND/NOR design > 4 Code converters|here=3]]

:::q <span class="tag">Manual Exp 3, aim</span>
Realise f(W, X, Y, Z) = Σm(1, 3, 5, 7, 8, 12, 14) using (i) basic gates, (ii) only NAND gates, (iii) only NOR gates.
:::

:::guess Guess first
Which form do you minimise for NAND-only, and which for NOR-only: SOP or POS?
:::

## Minimise

[[fig:kmap_f|K-map of f (the 1s). Blue: W'Z (m1, 3, 5, 7); red: WY'Z' (m8, 12); green: WXZ' (m12, 14).|w=50]]

$$f = W'Z + WY'Z' + WXZ'    (SOP, for basic gates and for NAND–NAND)$$

[[fig:kmap_fbar|K-map of f' (the 0s). Blue: W'Z'; red: WZ; green: WX'Y.|w=50]]

$$f' = W'Z' + WZ + WX'Y   ⇒   f = (W + Z)(W' + Z')(W' + X + Y')    (POS, for NOR–NOR)$$

**Rule:**

- SOP becomes **NAND–NAND**: replace every gate with a NAND, and keep the inverters.
- POS becomes **NOR–NOR**: replace every gate with a NOR.

[[fig:exp3_nand|NAND–NAND realisation of the SOP. The inverters W', Y', Z' are NANDs with their inputs tied.|w=70]]

[[fig:exp3_nor|NOR–NOR realisation of the POS.|w=70]]

## Wiring

| Form | Wires |
|---|---|
| **basic gates** | 7404: W → 1 → 2 (W'); Y → 3 → 4 (Y'); Z → 5 → 6 (Z'). 7408: 7404-2 → 1, Z → 2 → **3** (W'Z). 7411: W → 1, 7404-4 → 2, 7404-6 → 13 → **12** (WY'Z'); W → 3, X → 4, 7404-6 → 5 → **6** (WXZ'). 7432: 7408-3 → 1, 7411-12 → 2 → 3; 7432-3 → 4, 7411-6 → 5; **f = 7432-6** |
| **NAND only** | 7400: W → 1, 2 → 3 (W'); Y → 4, 5 → 6 (Y'); Z → 9, 10 → 8 (Z'); 7400-3 → 12, Z → 13 → **11**. 7410: W → 1, 7400-6 → 2, 7400-8 → 13 → **12**; W → 3, X → 4, 7400-8 → 5 → **6**; 7400-11 → 9, 7410-12 → 10, 7410-6 → 11; **f = 7410-8** |
| **NOR only** | 7402: W → 2, 3 → 1 (W'); Y → 5, 6 → 4 (Y'); Z → 8, 9 → 10 (Z'); W → 11, Z → 12 → **13** (W + Z)'. 7427: 7402-1 → 1, 7402-10 → 2, **GND → 13** → **12** (W' + Z')'; 7402-1 → 3, X → 4, 7402-4 → 5 → **6**; 7402-13 → 9, 7427-12 → 10, 7427-6 → 11; **f = 7427-8** |

[[fig:pin7410|7410 (3-input NAND); the 7411 (AND) and 7427 (NOR) share this layout.|w=42]]

## Truth table to verify

| WXYZ | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |

:::trap Trap: the spare NOR input
The 7427 has only 3-input NORs, and the term (W' + Z')' needs 2 inputs. Tie the third input to **GND**: 0 does not change an OR. Left floating, it reads as 1 and the gate's output sticks at 0.
:::

:::write Write in your record
**Result:** f = Σm(1, 3, 5, 7, 8, 12, 14) was minimised to f = W'Z + WY'Z' + WXZ' (SOP) and f = (W + Z)(W' + Z')(W' + X + Y') (POS). It was realised with basic gates, with NAND gates only and with NOR gates only, and all three circuits matched the truth table.

**Theory for the record:** a Boolean function is minimised with a K-map by grouping adjacent 1s (giving SOP) or 0s (giving POS) in powers of two. A two-level SOP (AND–OR) converts directly to NAND–NAND, and a POS (OR–AND) to NOR–NOR, by De Morgan's theorem. Inverters are made from NAND/NOR gates with their inputs tied. Universal-gate realisations need only one IC type.
:::

:::check Check 1
(a) Prove WY'Z' + WXZ' = WZ'(Y' + X) by K-map or algebra, and say why the pack keeps it as two terms. (b) In the NAND circuit, what is the output of the 7400 gate on pins 12–13 when W = 0, Z = 1? (c) Count the ICs in each version.
:::

<!--ANSWERS-->

## Answers

**Opening question.** NAND-only: **SOP** (AND–OR → NAND–NAND). NOR-only: **POS** (OR–AND → NOR–NOR).

**Check 1.** (a) Factor out WZ'. Keeping two terms gives a pure two-level circuit, which converts gate-for-gate to NAND–NAND. The factored form is three levels. (b) Inputs are W' = 1 and Z = 1, so NAND = **0**. The final NAND then outputs f = 1 ✓ (m1, m3, … all have W = 0, Z = 1). (c) Basic: 4 ICs (7404, 7408, 7411, 7432). NAND: 2 (7400, 7410). NOR: 2 (7402, 7427).

<!--/ANSWERS-->
