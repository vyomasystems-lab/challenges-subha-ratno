# challenges-subha-ratno
challenges-subha-ratno created by GitHub Classroom

# Level-1 Design-1 Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/54773800/181104843-e9a914ab-61a9-4458-a0d1-7e7d82864925.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes 31 2-bit inputs, a 5-bit select input *sel* and gives 2-bit output *out*.

The values are assigned to the input port using 
```
dut.sel.value = Sel;
dut.inp0.value = In0;
dut.inp1.value = In1;
dut.inp2.value = In2;
dut.inp3.value = In3;
dut.inp4.value = In4;
dut.inp5.value = In5;
dut.inp6.value = In6;
dut.inp7.value = In7;
dut.inp8.value = In8;
dut.inp9.value = In9;
dut.inp10.value = In10;
dut.inp11.value = In11;
dut.inp12.value = In12;
dut.inp13.value = In13;
dut.inp14.value = In14;
dut.inp15.value = In15;
dut.inp16.value = In16;
dut.inp17.value = In17;
dut.inp18.value = In18;
dut.inp19.value = In19;
dut.inp20.value = In20;
dut.inp21.value = In21;
dut.inp22.value = In22;
dut.inp23.value = In23;
dut.inp24.value = In24;
dut.inp25.value = In25;
dut.inp26.value = In26;
dut.inp27.value = In27;
dut.inp28.value = In28;
dut.inp29.value = In29;
dut.inp30.value = In30;
```

The assert statement is used for comparing the multiplexer's output to the expected value.

Here two test cases have been used.
### Test scenario 1
- Select line input: sel=5
- Particular input: inp5=3
- Expected output: out=3
- Observed output in the DUT dut.out=3

![inp5 given](https://user-images.githubusercontent.com/54773800/181118491-6de2d87d-a808-4d6b-8e3e-3f4c9a806274.png)

So no bug found for this test input.

### Test scenario 2
- Select line input: sel=30
- Particular input: inp30=2
- Expected output: out=2
- Observed output in the DUT dut.out=0

![inp30 given](https://user-images.githubusercontent.com/54773800/181118507-992bc3e8-6598-45e2-a843-228fc799ee5f.png)

Output mismatch for the above test input proves that there is a design bug.

## Design Bug
Based on the above test input and analysing the design, we see the following

```
begin
  case(sel)
    .
    .
    5'b11011: out = inp27;
    5'b11100: out = inp28;
    5'b11101: out = inp29;                    =====> BUG
    default: out = 0;
  endcase
 end
 ```
 
 For the multiplexer design, there is no matching case for ``inp30`` and so the output is given by the ``default: out = 0``
 
 ## Design Fix
 Updating the design and re-running the test makes the test pass.
 
 ![image](https://user-images.githubusercontent.com/54773800/181119359-7bafaf6d-c1dd-4730-bd53-b5f97637df51.png)
 
 The updated design is checked in as mux_fix.v
 
 ## Verification Strategy
 Here verification has been done by taking random value for the select line and fixed values for the input lines. Any mismatch in the output would signify a bug in the design of a particular line.
