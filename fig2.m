function[]=fig2()

% twocolumn revtex 4.1 format
%
% Figure 2: mean evacuation time
% 

figs;

[t,x,y]=statistics('out_fe_25_vd4_evacuacion.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.7 0 0.7]);
errorbar(log10(t),x,y);
plot(log10(t),x,'o');

clear t x y;


[t,x,y]=statistics('out_fe_100_vd4_evacuacion_simple.txt');
set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.9 0.6 0.0]);
errorbar(log10(t),x,y);
plot(log10(t),x,'s');

axis([0 10 200 700]);
xlabel('$\log_{10}(\epsilon)\,$(N.m)')
ylabel('$\langle t\rangle\,$(sec.)')


print -depsc2 fig2.eps


