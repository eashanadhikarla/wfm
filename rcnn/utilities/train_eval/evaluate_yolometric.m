clear
clc

ap1 = [];
recall1 = [];
precision1 = [];
ap2 = [];
recall2 = [];
precision2 = [];
ap3 = [];
recall3 = [];
precision3 = [];
for val_num=1:3
    dir_list = ls(['validation', num2str(val_num), '\textures\']);
    for ii= 1:10:length(dir_list)-2
        I = imread(['validation', num2str(val_num), '\textures\', dir_list(ii+2,:)]);
        texture_id = sscanf(dir_list(ii+2,:),'texture%d.png');
        load(['lda_results\validation', num2str(val_num), '\pruned_bbox', num2str(texture_id), '.mat'])
        results = table('Size',[1 2],...
                        'VariableTypes',{'cell','cell'},...
                        'VariableNames',{'Boxes','Scores'});
        results.Boxes{1} = bbox;
        results.Scores{1} = ones(size(bbox, 1), 1);
        
        bw = imread(['validation', num2str(val_num), '\masks\mask', num2str(texture_id), '.png']);
        S = regionprops(bw>0, 'boundingbox');
        gt_bbox = S.BoundingBox;
        gt_bbox_cell{1,1} = repmat(gt_bbox, 2, 1);
        a = [];
        for kk=1:2
            a = [a; 'lesion'];
        end
        a = string(a);
        gt_bbox_cell{1,2} = a;
        gt_bbox_table = cell2table(gt_bbox_cell);
        gt_blds = boxLabelDatastore(gt_bbox_table);
        
        [ap_temp,recall_temp,precision_temp] = evaluateDetectionPrecision(results, gt_blds, 0.5);
        ap1 = [ap1, ap_temp];
        recall1 = [recall1; recall_temp];
        precision1 = [precision1; precision_temp];
        
        [ap_temp,recall_temp,precision_temp] = evaluateDetectionPrecision(results, gt_blds, 0.75);
        ap2 = [ap2, ap_temp];
        recall2 = [recall2; recall_temp];
        precision2 = [precision3; precision_temp];
        
        for threshold=0.5:0.05:0.95
            [ap_temp,recall_temp,precision_temp] = evaluateDetectionPrecision(results, gt_blds, threshold);
            ap3 = [ap3, ap_temp];
        	recall3 = [recall3; recall_temp];
            precision3 = [precision3; precision_temp];
        end
    end
end


