function [Y,FS,NBITS,encoding_info,tag_info] = oggread(FILE)

a = length(FILE);
if a >= 4
    exten = FILE(a-3:a);
    if exten ~= '.ogg'
        FILE = strcat(FILE,'.ogg');
    end
end

if a <= 3
    FILE = strcat(FILE,'.ogg');
end
if exist(FILE) ~= 2
    error('File not Found')
end
%%%%%% 

s = which('oggread.m');
ff = findstr('oggread.m',s);
location = s(1:ff-2);
%%%%Temporary file%%%%%%
tmpfile = ['audio_ode_.wav'];

[stat_2,raw_data] = dos([location,'\oggdec', ' -o ', tmpfile, ' ', '"',FILE,'"']);
if stat_1 == 1 | stat_2 == 1
    error('Error while decoding file. File may be corrupted')
end
[Y,FS,NBITS] = wavread(tmpfile);    % Load the data and delete temporary file
delete(tmpfile);
