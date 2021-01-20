% celltype	techtype	typeIndex	rangeStart	rangeEnd
% axoaxoniccell	axoaxoniccell	0	0	1469
% bistratifiedcell	bistratifiedcell	1	1470	3679
% cckcell	cckcell	2	3680	7279
% ivycell	ivycell	3	7280	16089
% ngfcell	ngfcell	4	16090	19669
% olmcell	olmcell	5	19670	21309
%%% pyramidalcell	poolosyncell	6	21310	332809   %%% 7 %%% 
% pvbasketcell	pvbasketcell	7	332810	338339  
% scacell	scacell	8	338340	338739
% ca3cell	ppspont	9	338740	543439
% eccell	ppspont	10	543440	793439

clear
o=fopen ('teste.dat','wt');

xyz = load('xyz.dat'); % cell	x	y	z	host
celltype = load('celltype.dat'); %  typeIndex	rangeStart	rangeEnd

Deltaxyz = load('info_xyz.dat'); % cell	x	y	z	host

sizexyz = size(xyz);
sizecelltype = size(celltype);

Ntype=sizecelltype(1); % numero de typeIndex
N=sizexyz(1); % numero de neuronios

%dadosbin = zeros(size(vt));   
% nt=0;
Deltax= zeros(Ntype,4);
Deltay= zeros(Ntype,4);
Deltaz= zeros(Ntype,4);

for nt=1:Ntype
    for ii=celltype(nt,2)+1:celltype(nt,3)
        if xyz(ii+1,2)-xyz(ii,2)>0
            Deltax(nt,1)=xyz(ii+1,2)-xyz(ii,2);
            Deltax(nt,2)=xyz(ii+1,2);
            Deltax(nt,3)=xyz(ii,2);
            Deltax(nt,4)=ii+1;
        end
        if xyz(ii+1,3)-xyz(ii,3)>0
            Deltay(nt,1)=xyz(ii+1,3)-xyz(ii,3);
            Deltay(nt,2)=xyz(ii+1,3);
            Deltay(nt,3)=xyz(ii,3);
            Deltay(nt,4)=ii+1;
        end
        if xyz(ii+1,4)-xyz(ii,4)>0
            Deltaz(nt,1)=xyz(ii+1,4)-xyz(ii,4);
            Deltaz(nt,2)=xyz(ii+1,4);
            Deltaz(nt,3)=xyz(ii,4);
            Deltaz(nt,4)=ii+1;
        end
    end
end


xmax=4000.0;
ymax=976.0;

for nt=1:Ntype
    x=Deltaxyz(nt,1);
    y=Deltaxyz(nt,3);
    z=Deltaxyz(nt,5);
    fprintf(o,'%d %.1f %.1f %.0f\n',nt,x,y,z);
    aux=1;
    
    if(nt==7)
        ymax=920.0;
    else
        ymax=976.0;
    end
    
    if(nt>9)
        ymax=938.0;
    end
    
    rescale=1.0;
    scale=((celltype(nt,3)-celltype(nt,2))+1);%*rescale
    
    
    for ii=2:scale
        if(aux==Deltaxyz(nt,8)) %ultima camadas
            if(y+Deltaxyz(nt,4)<ymax) %2nd y-axis
                y=y+Deltaxyz(nt,4);
            else %3th x-axis
                x=x+Deltaxyz(nt,2);
                y=Deltaxyz(nt,3);
            end
            z=Deltaxyz(nt,5);
            aux=1;
        else %1st z-axis
            z=z+Deltaxyz(nt,6);
            aux=aux+1;
        end
        if(x<xmax*rescale)
            fprintf(o,'%d %.1f %.1f %.0f\n',nt,x,y,z);
        end
    end
end


% % nt=0;
% for ii = 1:338740
%     if nt==6
% %     fprintf(o,'%.2f %.2f %.2f %d\n',xyz(ii,2),xyz(ii,3),xyz(ii,4),1);
%     nada=0;
%     else
%     fprintf(o,'%.2f %.2f %.2f %d\n',xyz(ii,2),xyz(ii,3),xyz(ii,4),nt);
%     end
%     
%     if ii==(celltype(nt+1,3)+1) %  typeIndex rangeEnd
%         nt=nt+1;
%     end
% end

fclose(o);



% set style line 1 lc rgb "red"
% set style line 2 lc rgb "blue"
% set style line 3 lc rgb "green"
% set xrange [0:500]
% set yrange [0:500]
% splot 'savesss.dat' u 1:2:3:4 lc variable pt 7 ps 1 t"


