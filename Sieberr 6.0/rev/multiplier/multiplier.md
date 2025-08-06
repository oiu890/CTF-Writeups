# Challenge Details
Challenge name: Multiplier  
Competition: Sieberr 6.0  
Category: Reversing    
Points: 1000  
Solves: 3   
Author: fastfoodsworker  

# Challenge Description
an initial increase in spending prompts producers to produce at a greater output, generating more factor income for households which provide factors of production to these firms. these households then spend part of the additional income on consumer goods, while the rest of the additional income is saved, taxed or spent on imported goods. this generates a second round of increase in spending, which produces a second round of increase in factor income for households. this process continues until the increase in spending becomes negligible, hence leading to a greater increase in national income from an initial increase in spending.

# Files
![multiplier](./multiplier)

# Solve
We are given an executable binary file. Of course, the first step is to run it and see what happens.
![output](../../images/start.png)
Its some kind of multiplying numbers game so I just assumed that you have to win a certain amount of times to get a flag.
However, when you first run the file, it takes very long before showing you the output. It could be that theres something else going on.

Lets take a closer look:
![children](../../images/children.png)
:o :O :O :o 
The binary spawns a lot of children, but these children get deleted after the program finishes running.

# Ghidra
Of course, the next step would be to dump the binary into a decompiler of your choice and do some magic

uhhhhhhhhhhhhh
<details>
<summary>Decompiled</summary>
/* WARNING: Instruction at (ram,0x010e3200) overlaps instruction at (ram,0x010e31ff)
    */
/* WARNING: Removing unreachable block (ram,0x010e318b) */
/* WARNING: Removing unreachable block (ram,0x010e3193) */
/* WARNING: Removing unreachable block (ram,0x010e318f) */
/* WARNING: Removing unreachable block (ram,0x010e31e9) */
/* WARNING: Heritage AFTER dead removal. Example location: s0xffffffffffffffc0 : 0x010e3289 */
/* WARNING: Restarted to delay deadcode elimination for space: stack */

void processEntry entry(undefined8 param_1)

{
  ulong *puVar1;
  uint uVar2;
  uint uVar3;
  undefined8 uVar4;
  int iVar5;
  uint uVar6;
  undefined8 uVar7;
  int extraout_EDX;
  ulong uVar8;
  code *pcVar9;
  code *extraout_RDX;
  code *extraout_RDX_00;
  code *extraout_RDX_01;
  code *extraout_RDX_02;
  code *extraout_RDX_03;
  code *extraout_RDX_04;
  long lVar10;
  long *plVar11;
  undefined1 *puVar12;
  undefined1 *puVar13;
  long *plVar14;
  byte bVar15;
  byte bVar16;
  byte bVar17;
  undefined1 auVar18 [16];
  long local_d40 [415];
  undefined8 uStack_48;
  undefined *puStack_38;
  undefined *puStack_30;
  undefined *puStack_28;
  undefined8 local_20;
  long local_18;
  undefined8 uStack_10;
  long local_8;
  
  plVar11 = (long *)&stack0x00000008;
  do {
    lVar10 = *plVar11;
    plVar14 = plVar11 + 1;
    plVar11 = plVar11 + 1;
  } while (lVar10 != 0);
  do {
    plVar11 = plVar14 + 1;
    lVar10 = *plVar14;
    plVar14 = plVar11;
  } while (lVar10 != 0);
  uVar8 = 0x1000;
  do {
    puVar1 = (ulong *)(plVar11 + 1);
    lVar10 = *plVar11;
    if ((int)lVar10 == 0) goto LAB_010e3170;
    plVar11 = plVar11 + 2;
  } while ((int)lVar10 != 6);
  uVar8 = *puVar1 & 0xffffffff;
LAB_010e3170:
  local_8 = -uVar8;
  syscall();
  uVar4 = 0x13f;
  puStack_28 = &DAT_00c75000;
  local_18 = 0xcf3;
  local_20 = 0xffffffffffffffff;
  puStack_30 = &DAT_0046df18;
  puStack_38 = &DAT_00c7522c;
  uVar7 = 0;
  pcVar9 = FUN_010e32c7;
  lVar10 = -1;
  bVar17 = 0;
  bVar15 = 0;
  puVar12 = &DAT_010e32ec;
  plVar11 = local_d40;
  uStack_10 = param_1;
  do {
    while ((*pcVar9)(), pcVar9 = extraout_RDX, (bool)bVar15) {
      *(undefined1 *)plVar11 = *puVar12;
      puVar12 = puVar12 + (ulong)bVar17 * -2 + 1;
      plVar11 = (long *)((long)plVar11 + (ulong)bVar17 * -2 + 1);
    }
    do {
      uVar3 = (*pcVar9)();
      bVar15 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar15);
      uVar3 = (*extraout_RDX_00)();
      uVar6 = (uint)uVar7;
      pcVar9 = extraout_RDX_01;
    } while (!(bool)bVar15);
    bVar15 = uVar3 < 3;
    puVar13 = puVar12;
    if (!(bool)bVar15) {
      puVar13 = puVar12 + (ulong)bVar17 * -2 + 1;
      bVar15 = false;
      uVar3 = CONCAT31((int3)uVar3 + -3,*puVar12) ^ 0xffffffff;
      if (uVar3 == 0) {
        if (puVar13 == &DAT_010e3cc8) {
          local_d40[0] = local_8;
          lVar10 = local_18 + -0x10;
          do {
            iVar5 = FUN_010e32a8();
          } while (extraout_EDX != iVar5);
          lVar10 = FUN_010e32a8(0,lVar10,5);
          uStack_48 = 3;
          syscall();
                    /* WARNING: Could not recover jumptable at 0x010e32a6. Too many branches */
                    /* WARNING: Treating indirect jump as call */
          (*(code *)(lVar10 + 8))(uVar4);
          return;
        }
        do {
                    /* WARNING: Do nothing block with infinite loop */
        } while( true );
      }
      lVar10 = (long)(int)uVar3;
    }
    (*extraout_RDX_01)();
    bVar16 = CARRY4(uVar6,uVar6) || CARRY4(uVar6 * 2,(uint)bVar15);
    iVar5 = uVar6 * 2 + (uint)bVar15;
    auVar18 = (*extraout_RDX_02)();
    pcVar9 = auVar18._8_8_;
    uVar3 = auVar18._0_4_;
    uVar6 = iVar5 * 2 + (uint)bVar16;
    if (uVar6 == 0) {
      uVar8 = auVar18._0_8_ & 0xffffffff;
      bVar15 = 0xfffffffd < uVar3;
      do {
        uVar6 = (uint)uVar8;
        (*pcVar9)();
        uVar3 = (uint)bVar15;
        bVar15 = CARRY4(uVar6,uVar6) || CARRY4(uVar6 * 2,uVar3);
        uVar8 = (ulong)(uVar6 * 2 + uVar3);
        uVar3 = (*extraout_RDX_03)();
        uVar6 = (uint)uVar8;
        pcVar9 = extraout_RDX_04;
      } while (!(bool)bVar15);
    }
    uVar2 = (uint)((uint)lVar10 < 0xfffff300);
    bVar15 = CARRY4(uVar6,uVar3) || CARRY4(uVar6 + uVar3,uVar2);
    puVar12 = (undefined1 *)((long)plVar11 + lVar10);
    for (uVar8 = (ulong)(uVar6 + uVar3 + uVar2); uVar8 != 0; uVar8 = uVar8 - 1) {
      *(undefined1 *)plVar11 = *puVar12;
      puVar12 = puVar12 + (ulong)bVar17 * -2 + 1;
      plVar11 = (long *)((long)plVar11 + (ulong)bVar17 * -2 + 1);
    }
    uVar7 = 0;
    puVar12 = puVar13;
  } while( true );
}

</details>

We get a really really hard to read chunk of things and a bunch of warnings.
To make sense of it you can just ask an LLM for help.

# Fix
Turns out, the binary was packed.
We can unpack it by running the command 'upx -d filename'
![unpack](../../images/unpack.png)

Now back to ghidra

# Ghidra 2
![unpacked](../../images/mult1.png)
YES readable decompilation!!

Its quite easy to understand whats going on now, child98678016 is created, ran and then deleted.

The next step should be to access child98678016 to see what it does.
This can be done by running the original binary, then stopping the process with ctrl + Z.

# child98678016 (child1)
For simplicity we will call child98678016 child1

Looking at its decompilation:
![child1_1](../../images/child1.png)
and.... we face the same issue as before

After unpacking:
![child1_2](../../images/child1_2.png)
Much better :)
Similar as before, we do the same trick again and view the child:
![child2_1](../../images/child2_1.png)
AGAIN??!
![child2_2](../../images/child2_2.png)
oh...
We can assume that if we do this enough times, we would reach the final child file that has the flag.

Just now when we stopped the multiplier binary we actually dumped all the child files so lets take a look.

Running upx on all the children:
![upx_all](../../images/upx_all.png)
WAIT
child22385564 looks suspicious!!
Not counting the files that we had already unpacked previously (multiplier and the first 2 childs), child22385564 was not packed by UPX! IMPOSTER FOUND ඞඞඞඞඞඞඞඞඞඞ

![child_3](../../images/child3.png)
YAY we found the game logic as well as the flag code!!!!
However, we have to win the game ONE HUNDRED MILLION times to get the flag :(

Thankfully we can just patch the binary with ctrl+shift+g in ghidra

Let's set lcoal_30, which is the loop counter to 0x5f5e100, which is 100000000 in hex.
![patched](../../images/patched.png)
This skips the entire game lol
![for](../../images/for.png)
We then export the patched binary with format "Original File".
![export](../../images/export.png)

# Flag
Run the patched binary and flag.jpg will be put into your current folder
![flag](../../images/flag.jpg)
sctf{N3s71ng_ne5t1n6_0n3_7w0_7hr33}

This challenge was quite fun I learnt how to unpack and patch binaries
