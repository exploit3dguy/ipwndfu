.text

.pool


.set page_addr, 0x1800C8400
.set new_page, 0x60000100000625
.set old_page, 0x1000006A5


.global _main
_main:
msr daifset, #3
isb
ldr x0, =page_addr
ldr x6, =new_page
str x6, [x0]

bl flush_tlb

ldr x10, =0x100007924
ldr w6, =0xD503201F
str w6, [x10]

ldr x10, =0x10000792C
ldr w6, =0xD503201F
str w6, [x10]

ldr x10, =0x100007958
ldr w6, =0xD503201F
str w6, [x10]

ldr x10, =0x100007C9C
ldr w6, =0xD503201F
str w6, [x10]


ldr x0, =page_addr
ldr x6, =old_page
str x6, [x0]

bl flush_tlb

msr daifclr, #3
isb

ldr x10, =0x100000678
br x10

flush_tlb:
dsb sy
tlbi alle3
dsb sy
isb
ret

