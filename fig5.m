function[]=fig5()

% twocolumn revtex 4.1 format
%
% Figure 5: mean surviving couples
% 

% previuos procesing

%s=load('out_fe_25_vd4_broken.txt','-ascii');
%[n,m]=size(s);

%n1=1; n2=1; n3=1; n4=1; n5=1; n6=1;

%for i=1:n,
%  if s(i,2)==5,   s005(n1,1)=s(i,1); s005(n1,2)=s(i,4)/s(i,3); n1=n1+1; end
%  if s(i,2)==50,  s050(n2,1)=s(i,1); s050(n2,2)=s(i,4)/s(i,3); n2=n2+1; end
%  if s(i,2)==100, s100(n3,1)=s(i,1); s100(n3,2)=s(i,4)/s(i,3); n3=n3+1; end
%  if s(i,2)==150, s150(n4,1)=s(i,1); s150(n4,2)=s(i,4)/s(i,3); n4=n4+1; end
%  if s(i,2)==200, s200(n5,1)=s(i,1); s200(n5,2)=s(i,4)/s(i,3); n5=n5+1; end
%  if s(i,2)==250, s250(n6,1)=s(i,1); s250(n6,2)=s(i,4)/s(i,3); n6=n6+1; end
%end

%save('out_fe_25_vd4_broken_s005.txt','s005','-ascii');
%save('out_fe_25_vd4_broken_s050.txt','s050','-ascii');
%save('out_fe_25_vd4_broken_s100.txt','s100','-ascii');
%save('out_fe_25_vd4_broken_s150.txt','s150','-ascii');
%save('out_fe_25_vd4_broken_s200.txt','s200','-ascii');
%save('out_fe_25_vd4_broken_s250.txt','s250','-ascii');

figs;

[t,x,y]=statistics('out_fe_25_vd4_broken_s005.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.9 0.8 0]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'d');
axis([0 6 0 1.2])
xlabel('$\log_{10}(\epsilon)\,$(N.m)')
ylabel('survivability fraction')
clear t x y;

[t,x,y]=statistics('out_fe_25_vd4_broken_s050.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.9 0.6 0.0]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'s');

clear t x y;

[t,x,y]=statistics('out_fe_25_vd4_broken_s100.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[1 0.3 0.3]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'^');

clear t x y;

[t,x,y]=statistics('out_fe_25_vd4_broken_s150.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[1 0 0]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'>');

clear t x y;


[t,x,y]=statistics('out_fe_25_vd4_broken_s200.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.7 0 0.7]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'<');

clear t x y;

[t,x,y]=statistics('out_fe_25_vd4_broken_s250.txt');

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerFaceColor',[0.5 0.5 0.6]);
%errorbar(log10(t),x,y);
plot(log10(t),x);
plot(log10(t),x,'o');

clear t x y;




%[t,x,y]=statistics('out_fe_100_vd4_evacuacion.txt');
%set(0,'defaultLineMarker','none');
%errorbar(log10(t),x,y);
%plot(log10(t),x,'s');

%axis([0 10 200 700]);
%xlabel('$\log_{10}(\epsilon)\,$(N.m)')
%ylabel('$\langle t\rangle\,$(sec.)')


print -depsc2 fig3.eps


