import numpy as np
from scipy.integrate import solve_ivp
np.set_printoptions(precision=6)
print("== KVL loop 12V,2k,4k, 4V opposing")
i=(12-4)/6e3; print("i mA",i*1e3, "P: 12V supplies",12*i*1e3,"4V absorbs",4*i*1e3,"2k",i*i*2e3*1e3,"4k",i*i*4e3*1e3, "sum absorbed", (4*i+i*i*6e3)*1e3)
print("== mesh 10V,2k,4k(shared),2k,4V")
A=np.array([[6,-4],[-4,6]]);b=np.array([10,-4]); m=np.linalg.solve(A,b); print("i1,i2 mA",m,"shared",m[0]-m[1],"V",4*(m[0]-m[1]))
# nodal
G=1/2+1/4+1/2; V=(10/2+4/2)/G; print("nodal V",V)
print("== superposition circuit by mesh: 10V,4ohm,2ohm,2A up on right")
# mesh1 left (10V,4,2), mesh2 right has current source 2A: i2 = -2 (clockwise vs source up?) solve directly by nodal
VA=(10/4+2)/(1/4+1/2); print("VA",VA,"I",VA/2)
print("== two 5V sources across 1k: true I",5/1e3)
print("== Thevenin, 2I as 2 kOhm*I (mA,kOhm)")
def th(r):  # r = transresistance in ohms; R in ohms
    R=2000.
    # open circuit: unknown VA, I=(10-VA)/R ; I=(VA-r*I)/R
    # VA = (R+r) I ; 10-VA = R I -> I=10/(2R+r)
    I=10/(2*R+r); voc=(R+r)*I
    # short: I=(10-VA)/R ; I = (VA - r I)/R + VA/R  -> R I + r I = 2VA -> VA=(R+r)I/2 ; 10 = R I + VA
    I2=10/(R+(R+r)/2); VA2=(R+r)*I2/2; isc=VA2/R
    rth=voc/isc; IL=voc/(rth+1000)
    # full solve with RL: node A, node B
    # unknowns VA,VB,I: I=(10-VA)/R ; I = (VA - rI)/R + (VA-VB)/R ; (VA-VB)/R = VB/1000
    M=np.array([[1/R,0,1],[2/R,-1/R,-(1+r/R)],[1/R,-1/R-1/1000,0]]); rhs=np.array([10/R,0,0])
    VAf,VBf,If=np.linalg.solve(M,rhs)
    return voc,isc*1e3,rth,IL*1e3,VBf/1000*1e3
print("r=2k:",th(2000)); print("r=2ohm:",th(2))
print("== AC superposition: 10V DC + 10cos(1000t) series 1k + 1H")
I_ac=10/(1000+1j*1000); print("I_ac mA",abs(I_ac)*1e3,np.angle(I_ac,deg=True))
sol=solve_ivp(lambda t,x:[(10+10*np.cos(1000*t)-1000*x[0])/1.0],[0,0.05],[0.01],max_step=1e-5,dense_output=True)
t=np.linspace(0.04,0.05,5); print("sim",sol.sol(t)[0]*1e3); print("formula",(10+abs(I_ac)*1e3*np.cos(1000*t+np.angle(I_ac))))
print("== AC thevenin: 10V, 1k, C 1uF w=1000")
Zc=1/(1j*1000*1e-6); Vth=10*Zc/(1000+Zc); Zth=1000*Zc/(1000+Zc); IN=Vth/Zth
print("Vth",Vth,abs(Vth),np.angle(Vth,deg=True),"Zth",Zth,"IN mA",IN*1e3)
ZL=np.conj(Zth); I=Vth/(Zth+ZL); print("Pmax mW (peak phasors, 1/2 Re)",0.5*abs(I)**2*ZL.real*1e3)
best=max(((0.5*abs(Vth/(Zth+R+1j*X))**2*R*1e3,R,X) for R in np.linspace(100,1000,91) for X in np.linspace(0,1000,101))); print("sweep best",best)
print("== RC test signals R=1k C=1uF tau=1ms")
tau=1e-3
for name,u,f in [("step",lambda t:1.0,lambda t:1-np.exp(-t/tau)),("ramp",lambda t:t,lambda t:t-tau+tau*np.exp(-t/tau))]:
    s=solve_ivp(lambda t,x:[(u(t)-x[0])/tau],[0,5e-3],[0],max_step=1e-6,dense_output=True)
    tt=np.array([1e-3,3e-3]); print(name,"sim",s.sol(tt)[0],"formula",f(tt))
# impulse: approximate by 1 V*s pulse of width 1us
w=1e-6
s=solve_ivp(lambda t,x:[((1/w if t<w else 0)-x[0])/tau],[0,5e-3],[0],max_step=1e-7,dense_output=True)
tt=np.array([1e-3,3e-3]); print("impulse sim",s.sol(tt)[0],"formula",np.exp(-tt/tau)/tau)
print("== RL via Laplace = step: i(3us)",10*(1-np.exp(-3)))
print("== RLC series, L=1H, C=1uF, V=10 step")
L,C=1.0,1e-6
for R in [2500,2000,1200,0]:
    a=R/(2*L); w0=1/np.sqrt(L*C)
    s=solve_ivp(lambda t,x:[x[1]/C,(10-R*x[1]-x[0])/L],[0,0.012],[0,0],max_step=1e-6,dense_output=True,rtol=1e-9,atol=1e-12)
    tt=np.array([1e-3,2e-3,3.927e-3,5e-3])
    if R==2500: f=10-(40/3)*np.exp(-500*tt)+(10/3)*np.exp(-2000*tt)
    elif R==2000: f=10-10*(1+1000*tt)*np.exp(-1000*tt)
    elif R==1200: f=10-np.exp(-600*tt)*(10*np.cos(800*tt)+7.5*np.sin(800*tt))
    else: f=10*(1-np.cos(1000*tt))
    print(R,"alpha",a,"w0",w0,"roots",np.roots([1,R/L,1/(L*C)]),"\n  sim",s.sol(tt)[0],"\n  form",f)
    if R==1200:
        tp=np.pi/800; print("  peak vC",10*(1+np.exp(-600*tp)),"sim max",s.sol(np.linspace(0,0.012,200001))[0].max(), "i peak formula", "i(t)=12.5mA e^-600t sin800t, sim i(1ms)",s.sol(1e-3)[1]*1e3, 12.5*np.exp(-0.6)*np.sin(0.8))
print("== lumped: lambda 50Hz",3e8/50/1e3,"km ; 1GHz",3e8/1e9*100,"cm")
