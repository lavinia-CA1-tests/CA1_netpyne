nconex = conndatanew.VarName4;
nsyn = conndatanew.VarName5;
ncells = cellnumbersnew.VarName3;

j2=0;
for j=1:9
    for jj=1:9
        j2=j2+1;
        mc(j,jj)=nconex(j2)*ncells(jj);
        ms(j,jj)=nconex(j2)*ncells(jj)*nsyn(j2);
    end
end
