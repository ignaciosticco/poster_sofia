close all;

% formato para graficos en revtex 4.1
%
% a dos columnas: 3+3/8 (ancho, in)
% a una columna : 6.5   (ancho  in)

x0=0;                 % figure lower position
y0=0;                 % figure left position
width = 3+3/8;        % (in) two columnformat
height= width/1.618;  % (in) golden rectangle

set(0,'defaultFigurePaperUnits','inches');
set(0,'defaultFigurePosition',[x0 y0 width height]);
set(0,'DefaultFigurePaperPosition',[x0 y0 width height]);
set(0,'DefaultFigurePaperPositionMode','manual');

set(0,'defaultTextFontName','Times');
set(0,'defaultTextColor',[0 0 0]);
set(0,'defaultTextFontUnits','points');
set(0,'defaultTextFontSize',8);
set(0,'defaultTextFontWeight','normal');
set(0,'defaultTextVerticalAlignment','bottom');
set(0,'defaultTextHorizontalAlignment','left');
set(0,'defaultTextInterpreter','latex');

set(0,'defaultLineColor',[0 0 0]);  

set(0,'defaultLineLineStyle','-'); 
set(0,'defaultLineLineWidth',1.0);

set(0,'defaultLineMarker','none');
set(0,'defaultLineMarkerSize',5); 
set(0,'defaultLineMarker','o');
set(0,'defaultLineMarkerFaceColor',[1 1 1]);
set(0,'defaultLineMarkerEdgeColor',[0 0 0]);

set(0,'defaultAxesXcolor',[0, 0, 0]);
set(0,'defaultAxesYcolor',[0, 0, 0]);
set(0,'defaultAxesZcolor',[0, 0, 0]);
set(0,'defaultAxesColorOrder',[0 0 0]);

set(0,'defaultAxesLineWidth',0.5);

set(0,'defaultAxesFontUnits', 'points');
set(0,'defaultAxesFontName', 'Times');
set(0,'defaultAxesFontSize',9);

set(0,'defaultAxesUnits','normalized');
set(0,'defaultAxesPosition',[0.155 0.17 0.775 0.815]); 
set(0,'defaultAxesBox','on');

set(0,'DefaultAxesXGrid','on');
set(0,'DefaultAxesYGrid','on')
set(0,'defaultAxesGridLineStyle',':');

set(0,'DefaultAxesTickDir','in');

set(0,'defaultAxesNextPlot','add');

% Comentarios

% get(0,'default')
% set(0,'defaultAxesPosition',[0.13 0.11 0.775 0.815]);

