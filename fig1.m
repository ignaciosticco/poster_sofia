function[]=fig1()

% twocolumn revtex 4.1 format
%
% Figure 1: Fermi-like function 
% 

figs;


d=0.04;
e=1000;
c=1.16;

x=[0.7:0.001:1.6];
y=cosh((c-x)/(2*d)).^2;
y=e./(4*d*y);
maxy=max(y);

set(0,'defaultTextFontSize',10);
set(0,'defaultLineLineWidth',1.5);
set(0,'defaultAxesLineWidth',1.0);

plot(x,-y/maxy,'Color',[0.7 0.4 0.0])
axis([0.6 1.6 -1 0])
xlabel('$d\,$(m)')
text(0.75,-0.2,'$U/U_\mathrm{max}\rightarrow$','Color',[0.7 0.4 0.0]);
%ylabel('$f_a/f_\mathrm{max}$')
set(gca,'xtick',0.6:0.25:1.6);



x=[0.7:0.001:1.6];
y=1+exp((x-c)/d);
y=e./y;
maxy=max(y);

plot(x,-y/maxy,'Color',[0 0 0.5])
axis([0.6 1.6 -1 0])
xlabel('$d\,$(m)')
text(0.75,-0.99,'$f/f_\mathrm{max}\rightarrow$','Color',[0 0 0.5]);
%ylabel('$f_a/f_\mathrm{max}$')
set(gca,'xtick',0.6:0.25:1.6);



%t=[0.001:0.06:1.0];
%px=0.6*((1-t).^2)+2*(0.7-d/tanh((c-0.7)/(2*d)))*(t.*(1-t))+0.7*t.^2;
%py=(e/(4*d*(cosh((c-0.7)/(2*d))^2)))*t.^2;

%maxy=max(py);

%plot(px,py/maxy,'--')

%x1=0.6*((1-0.001)^2)+2*(0.7-d/tanh((c-0.7)/(2*d)))*(0.001*(1-0.001))+0.7*0.001^2;
%y1=(e/(4*d*(cosh((c-0.7)/(2*d))^2)))*0.001^2;
%x2=0.7;
%y2=(e/(4*d*(cosh((c-0.7)/(2*d))^2)));

%plot([x1 x2],[y1 y2]/maxy,'o')

%fx=[0.6:0.001:1.6];
%fy=2000*exp((0.6-fx)/0.08);

%plot(fx,log(fy/1000),'--')

%fx=[0.6:0.1:1.6];
%fy=2000*exp((0.6-fx)/0.08);

%plot(fx,log(fy/1000),'square')

print -depsc2 fig1b.eps


