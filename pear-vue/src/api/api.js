import {getAction, deleteAction, putAction, postAction} from '@/api/manage'

const getStar = (params) => getAction('/star/', params);

const duplicateCheck = (params)=>getAction("/sys/duplicate/check",params);


export {
    getStar,
    duplicateCheck,
}



