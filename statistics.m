function [t,x,y] = statistics(myfile)

%
% media y varianza de las mediciones 
% ingresar el nombre del archivo 'file.txt'
%

s=load(myfile,'-ascii');
[n,m]=size(s);

[t,ii,jj]=unique(s(1:n,1));
[ni,mi]=size(ii);

for i=2:m,
    x(1:ni,i-1)=accumarray(jj,s(1:n,i),[],@mean);
    y(1:ni,i-1)=accumarray(jj,s(1:n,i),[],@std);
end

end

