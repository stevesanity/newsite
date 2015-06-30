/**
 * Created by xls on 15/5/15.
 */
$(document).ready(function() {
(function () {
        "use strict";

        FHIR.oauth2.ready(function(smart){
            var patient = smart.context.patient;

            patient.read().then(function(pt) {

                var name =
                        pt.name[0].given.join(" ") + " " +
                        pt.name[0].family.join(" ") ;




                document.getElementById('name').innerHTML = name;

                $("#Health-alert").bind('click',function() {
                    $(this).unbind('click');
                    patient.MedicationPrescription
                        .search()
                        .then(function (prescriptions) {

                            var med_list = document.getElementById('med_list');

                            prescriptions.forEach(function (prescription) {
                                var meds = prescription.contained;
                                meds.forEach(function (med) {
                                    med_list.innerHTML += "<li> " + med.name + "</li>";
                                });
                            });

                        });
                });


                $("#Vital-sign-record").bind('click',function() {
                    $(this).unbind('click');
                    patient.Observation
                        .search()
                        .then(function(prescription) {

                            var med_list = document.getElementById('vital_sign');

                            var meds = prescription;
                            meds.forEach(function (med) {
                                med_list.innerHTML += "<li> " + med.text.div + "</li>";
                            })


                        })
                        })



                /*patient.MedicationPrescription
                        .search()
                        .then(function(pr){
                            var medlist = pr.resourceType;
                            document.getElementById('vital_sign').innerHTML = medlist;
                        })*/



                /*patient.Observation
                        .search()
                        .then(function(Observation) {
                            var vital_sign = document.getElementById('vital_sign');

                            Observation.forEach(function(Observation){
                                var signs = Observation.related;
                                signs.forEach(function(med){
                                    vital_sign.innerHTML += "<li> " + med + "</li>"
                                })
                            })
                        })*/

            });
        });

    }());
});