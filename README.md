# challenges-subha-ratno
challenges-subha-ratno created by GitHub Classroom

# Design-1 Verification
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

Here two 
